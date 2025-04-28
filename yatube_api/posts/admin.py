from django.contrib import admin
from .models import Post, Comment, Group, Follow


@admin.register(Post, Comment, Group, Follow)
class PostsAdmin(admin.ModelAdmin):
    pass
