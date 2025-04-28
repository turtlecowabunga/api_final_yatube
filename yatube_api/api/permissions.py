from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    "Авторизация автора модели или только для чтения."
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.author
