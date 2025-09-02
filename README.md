# 📌 TeraStore API

This project is a Django REST Framework backend API for an e-commerce platform, specifically a tech store. It provides a robust and scalable API for managing products, categories, and other e-commerce-related data. The API is designed to be consumed by a separate frontend application.

-----

## ✨ Features

  - **Product Management:** Retrieve a list of all products or details for a single product.
  - **Category-based Filtering:** Fetch products based on their category.
  - **Category Listing:** Get a list of all available product categories.
  - **Admin Portal:** Manage products and categories through the built-in Django Admin interface.
  - **RESTful Endpoints:** Well-defined API endpoints for seamless integration with a frontend.

-----

## 🛠️ Tech Stack

  - **Python**
  - **Django**: A high-level Python web framework for rapid development.
  - **Django REST Framework**: A powerful toolkit for building Web APIs.
  - **django-cors-headers**: A Django app for handling Cross-Origin Resource Sharing (CORS).
  - **Pillow**: The Python Imaging Library, used for image processing.

-----

## 📁 Folder Structure

```
terastore/
├── terastore/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── products/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
└── requirements.txt
```

-----

## 🚀 How to Run

To get this project up and running on your local machine, follow these steps:

1.  **Clone the repository**
    ```bash
    git clone https://github.com/FAHAD-ALI-github/terastore-DRF-API.git
    ```
2.  **Navigate into the project directory**
    ```bash
    cd terastore-DRF-API
    ```
3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run migrations**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
5.  **Create a superuser to access the admin portal**
    ```bash
    python manage.py createsuperuser
    ```
6.  **Run the development server**
    ```bash
    python manage.py runserver
    ```
    The API will be available at `http://127.0.0.1:8000/`.

-----


## 🌐 Live Demo

[🔗 Live Site](https://tera-tech-store.vercel.app/)

-----

## 👤 Author

**Fahad Ali** \* GitHub: [@FAHAD-ALI-github](https://github.com/FAHAD-ALI-github)

  * LinkedIn: [fahadali1078](https://www.linkedin.com/in/fahadali1078/)
