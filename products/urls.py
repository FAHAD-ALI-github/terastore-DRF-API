from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/<int:id>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('products/category/', views.products_by_category, name='products-by-category'),
    path('categories/', views.category_list, name='category-list'),
]
