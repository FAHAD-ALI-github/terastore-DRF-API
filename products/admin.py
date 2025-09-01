from django.contrib import admin
from .models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']
    ordering = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'category', 'brand', 'discount', 'created_at']
    list_filter = ['category', 'brand', 'created_at']
    search_fields = ['title', 'brand', 'model']
    list_editable = ['price', 'discount']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'category')
        }),
        ('Pricing & Discount', {
            'fields': ('price', 'discount')
        }),
        ('Product Details', {
            'fields': ('brand', 'model', 'image')
        }),
    )
