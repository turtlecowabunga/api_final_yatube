from rest_framework.pagination import LimitOffsetPagination
from rest_framework import mixins, viewsets, serializers
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.filters import SearchFilter

from django.shortcuts import get_object_or_404
from django.db.utils import IntegrityError

from posts.models import Post, Group

from .serializers import (PostSerializer, CommentSerializer,
                          GroupSerializer, FollowSerializer)

from .permissions import IsAuthorOrReadOnly


class CreateListViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    pass


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly)

    def get_post_instance(self):
        post_id = self.kwargs.get('post_id')
        return get_object_or_404(Post, pk=post_id)

    def perform_create(self, serializer):
        serializer.save(
            post=self.get_post_instance(),
            author=self.request.user
        )

    def get_queryset(self):
        post_instance = self.get_post_instance()
        return post_instance.comments.all()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class FollowViewSet(CreateListViewSet):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter,)
    search_fields = ('following__username',)

    def perform_create(self, serializer):
        following = serializer.validated_data.get('following')
        if self.request.user == following:
            raise serializers.ValidationError(
                {'following': 'Вы не можете подписаться на самого себя.'}
            )
        try:
            serializer.save(user=self.request.user)
        except IntegrityError:
            raise serializers.ValidationError(
                {'following': f'Вы уже подписаны на {following}.'}
            )

    def get_queryset(self):
        return self.request.user.followings
