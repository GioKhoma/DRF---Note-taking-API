<<<<<<< HEAD
# E-Commerce API with Django Rest Framework

Welcome to the **E-Commerce API** project! This repository contains a backend application built using Django and Django Rest Framework, designed to provide a robust API for an e-commerce platform. The API supports various functionalities necessary for managing an online store, including product management, user authentication, and order processing.

## Features

- **User Authentication**: Register, login, and manage user accounts with token-based authentication.
- **Product Management**: Create, update, delete, and view products with detailed information.
- **Category Management**: Organize products into categories for better navigation.
- **Cart and Order Management**: Add products to the cart, create orders, and track order status.
- **Payment Processing**: Integration with payment gateways for seamless transactions (example placeholder, actual implementation may vary).
- **Admin Panel**: Manage the platform using Django's built-in admin interface.

## Technologies Used

- **Django**: High-level Python web framework.
- **Django Rest Framework**: Powerful and flexible toolkit for building Web APIs.
- **SQLite**: Default database for development (can be switched to PostgreSQL or MySQL for production).
- **JWT**: JSON Web Token for user authentication.
- **Docker**: Containerization of the application for easy deployment.

## Getting Started

### Prerequisites

- Python 3.8+
- Docker (optional but recommended for containerization)
- Virtual environment tool (e.g., `venv` or `virtualenv`)

### Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-username/e-commerce-api.git
   cd e-commerce-api

=======
E-Commerce API
Welcome to the E-Commerce API project! This project is built using Django and Django Rest Framework to provide a robust backend for an e-commerce platform. The API supports various functionalities necessary for managing an online store, including product management, user authentication, and order processing.

Features
User Authentication: Register, login, and manage user accounts with token-based authentication.
Product Management: Create, update, delete, and view products with detailed information.
Category Management: Organize products into categories for better navigation.
Cart and Order Management: Add products to the cart, create orders, and track order status.
Payment Processing: Integration with payment gateways for seamless transactions (example placeholder, actual implementation may vary).
Admin Panel: Manage the platform using Django's built-in admin interface.
Technologies Used
Django: High-level Python web framework.
Django Rest Framework: Powerful and flexible toolkit for building Web APIs.
SQLite: Default database for development (can be switched to PostgreSQL or MySQL for production).
JWT: JSON Web Token for user authentication.
Docker: Containerization of the application for easy deployment.

Getting Started
Prerequisites
Python 3.8+
Docker (optional but recommended for containerization)
Virtual environment tool (e.g., venv or virtualenv)

Installation

Clone the repository:

git clone https://github.com/your-username/e-commerce-api.git
cd e-commerce-api

Create and activate a virtual environment:

python -m venv venv
source venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Apply migrations:

python manage.py migrate

Create a superuser:

python manage.py createsuperuser
Run the development server:

python manage.py runserver


API Endpoints
The API follows RESTful principles and includes the following endpoints:

Profiles
GET /api/_profiles/: List all profiles.
POST /api/_profiles/: Create a new profile.
GET /api/_profiles/{id}/: Retrieve a single profile by ID.
PUT /api/_profiles/{id}/: Update an existing profile.
PATCH /api/_profiles/{id}/: Partially update a profile.
DELETE /api/_profiles/{id}/: Delete a profile.
Carts
GET /api/carts/: List all carts.
POST /api/carts/: Create a new cart.
GET /api/carts/{cartt_pk}/items/: List all items in a cart.
POST /api/carts/{cartt_pk}/items/: Add an item to a cart.
GET /api/carts/{cartt_pk}/items/{id}/: Retrieve a single item in a cart by ID.
PATCH /api/carts/{cartt_pk}/items/{id}/: Partially update an item in a cart.
DELETE /api/carts/{cartt_pk}/items/{id}/: Delete an item from a cart.
GET /api/carts/{id}/: Retrieve a single cart by ID.
DELETE /api/carts/{id}/: Delete a cart.
Categories
GET /api/categories/: List all categories.
POST /api/categories/: Create a new category.
GET /api/categories/{category_id}/: Retrieve a single category by ID.
PUT /api/categories/{category_id}/: Update an existing category.
PATCH /api/categories/{category_id}/: Partially update a category.
DELETE /api/categories/{category_id}/: Delete a category.
Orders
GET /api/orders/: List all orders.
POST /api/orders/: Create a new order.
GET /api/orders/{id}/: Retrieve a single order by ID.
PUT /api/orders/{id}/: Update an existing order.
PATCH /api/orders/{id}/: Partially update an order.
DELETE /api/orders/{id}/: Delete an order.
Products
GET /api/products/: List all products.
POST /api/products/: Create a new product.
GET /api/products/{id}/: Retrieve a single product by ID.
PUT /api/products/{id}/: Update an existing product.
PATCH /api/products/{id}/: Partially update a product.
DELETE /api/products/{id}/: Delete a product.
GET /api/products/{productt_pk}/reviews/: List all reviews for a product.
POST /api/products/{productt_pk}/reviews/: Create a new review for a product.
GET /api/products/{productt_pk}/reviews/{id}/: Retrieve a single review by ID.
PUT /api/products/{productt_pk}/reviews/{id}/: Update an existing review.
PATCH /api/products/{productt_pk}/reviews/{id}/: Partially update a review.
DELETE /api/products/{productt_pk}/reviews/{id}/: Delete a review.
Authentication
POST /auth/jwt/create/: Create JWT.
POST /auth/jwt/refresh/: Refresh JWT.
POST /auth/jwt/verify/: Verify JWT.
GET /auth/users/: List all users.
POST /auth/users/: Create a new user.
POST /auth/users/activation/: Activate a user account.
GET /auth/users/me/: Retrieve the current user's profile.
PUT /auth/users/me/: Update the current user's profile.
PATCH /auth/users/me/: Partially update the current user's profile.
DELETE /auth/users/me/: Delete the current user's profile.
POST /auth/users/resend_activation/: Resend activation email.
POST /auth/users/reset_password/: Reset password.
POST /auth/users/reset_password_confirm/: Confirm password reset.
POST /auth/users/reset_username/: Reset username.
POST /auth/users/reset_username_confirm/: Confirm username reset.
POST /auth/users/set_password/: Set a new password.
POST /auth/users/set_username/: Set a new username.
GET /auth/users/{id}/: Retrieve a single user by ID.
PUT /auth/users/{id}/: Update an existing user.
PATCH /auth/users/{id}/: Partially update a user.
DELETE /auth/users/{id}/: Delete a user.
>>>>>>> ca22e7cacc54384f6d468912ccc35f68e6fa2fa0
