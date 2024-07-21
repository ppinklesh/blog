from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post, Comment
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

# Helper function to get JWT token
def get_token_for_user(user):
    refresh = RefreshToken.for_user(user)
    return str(refresh.access_token)

# Model Tests
class BlogModelTests(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
    
    def test_post_creation(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.content, 'Test Content')
        self.assertEqual(post.author.username, 'testuser')
    
    def test_comment_creation(self):
        comment = Comment.objects.create(post=self.post, author=self.user, text='Test Comment')
        self.assertEqual(comment.post.title, 'Test Post')
        self.assertEqual(comment.author.username, 'testuser')
        self.assertEqual(comment.text, 'Test Comment')

# API View Tests
class BlogAPITests(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = get_token_for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        for i in range(15):  # Creating 15 posts to test pagination
            Post.objects.create(title=f'Test Post {i}', content='Test Content {i}', author=self.user)

    def test_create_post(self):
        url = reverse('post-list-create')
        data = {'title': 'New Post', 'content': 'New Content'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 16)
        self.assertEqual(Post.objects.get(id=16).title, 'New Post')
    
    def test_get_post_list(self):
        url = reverse('post-list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check the total count of items in the response
        self.assertEqual(response.data['count'], 15)  # total number of posts
        
        # Check the number of items on the first page
        self.assertEqual(len(response.data['results']), 10)  # number of posts on the first page

        # Check the number of items on the second page
        response = self.client.get('/api/posts/?page=2')
        self.assertEqual(len(response.data['results']), 5)  # number of posts on the second page
    
    def test_get_post_detail(self):
        post = Post.objects.first()
        url = reverse('post-detail', args=[post.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], post.title)
    
    def test_update_post(self):
        post = Post.objects.first()
        url = reverse('post-detail', args=[post.id])
        data = {'title': 'Updated Post', 'content': 'Updated Content'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        post.refresh_from_db()
        self.assertEqual(post.title, 'Updated Post')
    
    def test_delete_post(self):
        post = Post.objects.first()
        url = reverse('post-detail', args=[post.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 14)
    
    def test_create_comment(self):
        post = Post.objects.first()
        url = reverse('comment-list-create', args=[post.id])
        data = {'text': 'New Comment'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(Comment.objects.get(id=1).text, 'New Comment')
    
    def test_get_comment_list(self):
        post = Post.objects.first()
        Comment.objects.create(post=post, author=self.user, text='Test Comment')
        url = reverse('comment-list-create', args=[post.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_like_post(self):
        post = Post.objects.first()
        url = reverse('like-post', args=[post.id])
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['likes_count'], 1)
        post.refresh_from_db()
        self.assertEqual(post.likes.count(), 1)
