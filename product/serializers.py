from rest_framework import serializers
from .models import Category, Product, Review
from rest_framework.exceptions import ValidationError

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


class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length = 1, max_length=255)


class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1, max_length=255)
    description = serializers.CharField(min_length=1, max_length=255)
    category_id = serializers.IntegerField()

    def validate_category_id(self, category_id):
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError('Category does not exist!')
        return category_id

class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(min_length=1, max_length=255)
    product_id = serializers.IntegerField()
    stars = serializers.IntegerField(min_value=1, max_value=5)

    def validate_product_id(self, product_id):
        try:
            Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise ValidationError('Product does not exist!')
        return product_id



    
    


