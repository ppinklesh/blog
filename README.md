```markdown
# Django Blog Application

## Introduction
This is a simple blog application built using Django and Django REST Framework. The application includes functionalities for creating, reading, updating, and deleting posts and comments. User authentication is handled using JSON Web Tokens (JWT).

## Features
- User registration and login
- Create, read, update, and delete posts
- Create and read comments for each post
- Like and unlike posts
- Token-based authentication
- Pagination for the list of posts

## Setup Instructions

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Installation

2. Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```sh
   python manage.py runserver
   ```

## API Documentation

### User Registration
- **Endpoint:** `/api/register/`
- **Method:** `POST`
- **Payload:**
  ```json
  {
      "username": "newuser",
      "password": "newpassword",
      "email": "newuser@example.com",
      "first_name": "New",
      "last_name": "User"
  }
  ```
- **Response:**
  ```json
  {
      "username": "newuser",
      "email": "newuser@example.com",
      "access": "your-access-token",
      "refresh": "your-refresh-token"
  }
  ```

### User Login
- **Endpoint:** `/api/token/`
- **Method:** `POST`
- **Payload:**
  ```json
  {
      "username": "newuser",
      "password": "newpassword"
  }
  ```
- **Response:**
  ```json
  {
      "access": "your-access-token",
      "refresh": "your-refresh-token"
  }
  ```

### Refresh Token
- **Endpoint:** `/api/token/refresh/`
- **Method:** `POST`
- **Payload:**
  ```json
  {
      "refresh": "your-refresh-token"
  }
  ```
- **Response:**
  ```json
  {
      "access": "your-new-access-token"
  }
  ```

### List Posts
- **Endpoint:** `/api/posts/`
- **Method:** `GET`
- **Response:**
  ```json
  {
      "count": 15,
      "next": "http://example.com/api/posts/?page=2",
      "previous": null,
      "results": [
          {
              "id": 1,
              "title": "First Post",
              "content": "This is the content of the first post.",
              "author": "newuser",
              "published_date": "2023-07-21T12:34:56Z",
              "likes": [],
              "likes_count": 0
          },
          // ... 9 more posts
      ]
  }
  ```

### Create Post
- **Endpoint:** `/api/posts/`
- **Method:** `POST`
- **Payload:**
  ```json
  {
      "title": "New Post",
      "content": "This is the content of the new post."
  }
  ```
- **Response:**
  ```json
  {
      "id": 1,
      "title": "New Post",
      "content": "This is the content of the new post.",
      "author": "newuser",
      "published_date": "2023-07-21T12:34:56Z",
      "likes": [],
      "likes_count": 0
  }
  ```

### Retrieve Post
- **Endpoint:** `/api/posts/<int:pk>/`
- **Method:** `GET`
- **Response:**
  ```json
  {
      "id": 1,
      "title": "First Post",
      "content": "This is the content of the first post.",
      "author": "newuser",
      "published_date": "2023-07-21T12:34:56Z",
      "likes": [],
      "likes_count": 0
  }
  ```

### Update Post
- **Endpoint:** `/api/posts/<int:pk>/`
- **Method:** `PUT`
- **Payload:**
  ```json
  {
      "title": "Updated Post",
      "content": "This is the updated content of the post."
  }
  ```
- **Response:**
  ```json
  {
      "id": 1,
      "title": "Updated Post",
      "content": "This is the updated content of the post.",
      "author": "newuser",
      "published_date": "2023-07-21T12:34:56Z",
      "likes": [],
      "likes_count": 0
  }
  ```

### Delete Post
- **Endpoint:** `/api/posts/<int:pk>/`
- **Method:** `DELETE`
- **Response:** `204 No Content`

### List Comments for a Post
- **Endpoint:** `/api/posts/<int:post_id>/comments/`
- **Method:** `GET`

## Running Tests

To run the tests, execute the following command:
```sh
python manage.py test
```
```