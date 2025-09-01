from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        return Product.objects.select_related('category').all()
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        
        # Return in FakeStore API format
        return Response({
            "status": "SUCCESS",
            "message": "Products fetched successfully",
            "products": serializer.data
        })

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.select_related('category')
    serializer_class = ProductSerializer
    lookup_field = 'id'
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        
        # Return in FakeStore API format
        return Response({
            "status": "SUCCESS", 
            "message": "Product fetched successfully",
            "product": serializer.data
        })

@api_view(['GET'])
def products_by_category(request):
    category_type = request.GET.get('type')
    
    if not category_type:
        return Response({
            "status": "ERROR",
            "message": "Category type parameter is required"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        category = Category.objects.get(name__iexact=category_type)
        products = Product.objects.filter(category=category).select_related('category')
        serializer = ProductSerializer(products, many=True)
        
        return Response({
            "status": "SUCCESS",
            "message": "Products fetched successfully",
            "products": serializer.data
        })
    except Category.DoesNotExist:
        return Response({
            "status": "ERROR", 
            "message": "Category not found",
            "products": []
        })

@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    
    return Response({
        "status": "SUCCESS",
        "categories": serializer.data
    })