# blog/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Custom user model extending the default AbstractUser."""
    pass


class Post(models.Model):
    """Model representing a blog post."""
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(CustomUser, related_name='liked_posts', blank=True)

    class Meta:
        """Meta options for Post model."""
        ordering = ['-published_date']  # Default ordering by published_date in descending order

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Model representing a comment on a blog post."""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta options for Comment model."""
        ordering = ['created_date']  # Default ordering by created_date in ascending order

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
