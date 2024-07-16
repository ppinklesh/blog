# Blog Application

## Setup Instructions

1. Clone the repository:
    ```sh
    git clone https://github.com/ppinklesh/blog.git
    ```

2. Navigate to the project directory:
    ```sh
    cd blog_project
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply the migrations:
    ```sh
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

7. Access the API at `http://127.0.0.1:8000/api/`
