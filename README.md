The E-commerce Product API is a Web based  service designed for managing an e-commerce platform's product catalog. 
This API enables users to perform CRUD operations (Create, Read, Update, Delete) on products, 
search for products by name or category, and authenticate users to secure operations. 
Built with Django REST Framework, it provides scalable, secure, and efficient functionality for any e-commerce application.


**E-commerce API**

A Django-based API for E-commerce. This project is part of the Backend Capstone preparation.

**Authentication Setup**

This project uses Django REST Framework to implement API authentication.

**Authentication Methods**

JWT Authentication

Generate a token: POST /api/token/
Refresh a token: POST /api/token/refresh/

**Token Authentication (Optional)**

Generate a token for a user: python manage.py drf_create_token <username>

**Testing the API**

Obtain a JWT Token

Send a POST request to /api/token/ with the following body:

{
  "username": "your_username",
  "password": "your_password"
}

Example Response:

{
  "access": "your_access_token",
  "refresh": "your_refresh_token"
}

**Access Secure Endpoints**

Add the following header to requests:
Authorization: Bearer your_access_token
Refresh the Token

Send a POST request to /api/token/refresh/ with the following body:

{
  "refresh": "your_refresh_token"
}

**Push Your Changes to GitHub**
 
**Commit your changes:**

git add .

git commit -m "Add authentication to API"
