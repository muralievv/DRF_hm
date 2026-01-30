from rest_framework import serializers
from .models import Category, Product, Review

class CategoryListSerializer(serializers.ModelSerializer):
    products_count = serializers.ReadOnlyField()
    class Meta:
        model = Category
        fields = ['id', 'name', 'products_count']

class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.name')
    class Meta:
        model = Product
        fields = ['id', 'title','description','category', 'average_rating']
    

class ReviewListSerializer(serializers.ModelSerializer):
    average_rating = serializers.ReadOnlyField(source='product.average_rating')
    
    product = serializers.ReadOnlyField(source='product.title')
    class Meta:
        model = Review
        fields = ['text', 'product', 'stars', 'average_rating']

    
    


