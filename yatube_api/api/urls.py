from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

router_v1 = SimpleRouter()
router_v1.register('posts', views.PostViewSet, basename='post')
router_v1.register(r'posts/(?P<post_id>\d+)/comments',
                   views.CommentViewSet, basename='comment')
router_v1.register('groups', views.GroupViewSet, basename='group')
router_v1.register('follow', views.FollowViewSet, basename='following')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
