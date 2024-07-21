# blog/admin.py

from django.contrib import admin
from .models import CustomUser, Post, Comment
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    pass

admin.site.register(CustomUser, CustomUserAdmin)

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'likes_count')
    search_fields = ('title', 'content', 'author__username')
    list_filter = ('published_date', 'author')
    inlines = [CommentInline]

    def likes_count(self, obj):
        return obj.likes.count()
    likes_count.short_description = 'Likes'

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_date', 'text')
    search_fields = ('author__username', 'text')
    list_filter = ('created_date', 'author')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
