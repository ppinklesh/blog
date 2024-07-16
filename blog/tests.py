from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment

class PostModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='12345')
        Post.objects.create(title='Test Post', content='Test Content', author=user)

    def test_post_creation(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.content, 'Test Content')

class CommentModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='12345')
        post = Post.objects.create(title='Test Post', content='Test Content', author=user)
        Comment.objects.create(post=post, author='Test Commenter', text='Test Comment')

    def test_comment_creation(self):
        comment = Comment.objects.get(id=1)
        self.assertEqual(comment.text, 'Test Comment')
