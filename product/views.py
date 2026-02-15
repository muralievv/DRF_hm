from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Category, Review
from .serializers import CategoryListSerializer, ProductListSerializer, ReviewListSerializer, CategoryValidateSerializer, ProductValidateSerializer, ReviewValidateSerializer
from django.db import transaction
from rest_framework.viewsets import ModelViewSet

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ReviewListSerializer
        return ReviewValidateSerializer

# @api_view(['GET', 'POST'])
# def categories_list_api_view(request):
#     if request.method == 'GET':
#         categories = Category.objects.all()
#         data = CategoryListSerializer(instance=categories, many=True).data
#         return Response(
#             status=status.HTTP_200_OK,
#             data=data
#         )
#     elif request.method == 'POST':
#         serializer = CategoryValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
#         name = serializer.validated_data.get('name')
#         category = Category.objects.create(
#             name=name
#         )
#         return Response(status=status.HTTP_201_CREATED,
#        data=CategoryListSerializer(category).data)
        

# @api_view(['GET', 'PUT','DELETE'])
# def category_detail_api_view(request, id):
#     category = get_object_or_404(Category, id=id)
#     if request.method == 'GET':
#         data = CategoryListSerializer(instance=category, many=False).data
#         return Response(
#             status=status.HTTP_200_OK,
#             data=data
#         )
#     elif request.method == 'PUT':
#         serializer = CategoryValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
#         category.name = serializer.validated_data.get('name')
#         category.save()
#         return Response(status=status.HTTP_201_CREATED, data = CategoryListSerializer(category).data)
#     elif request.method == 'DELETE':
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET','POST'])
# def product_list_api_view(request):
#     if request.method == 'GET':
#         products = Product.objects.all()
#         data = ProductListSerializer(instance=products, many=True).data
#         return Response(
#             status=status.HTTP_200_OK,
#             data=data
#         )
#     elif request.method == 'POST':
#         serializer = ProductValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
#         title = serializer.validated_data.get('title')
#         description = serializer.validated_data.get('description')
#         category_id = serializer.validated_data.get('category_id')
#         with transaction.atomic():
#             product = Product.objects.create(
#                 title=title,
#                 description=description,
#                 category_id=category_id
#             )
#         return Response(status=status.HTTP_201_CREATED,
#                         data=ProductListSerializer(product).data)

# @api_view(['GET', 'PUT', 'DELETE'])
# def product_detail_api_view(request, id):
#     product = get_object_or_404(Product, id=id)
#     if request.method == 'GET':
#         data = ProductListSerializer(instance=product, many=False).data
#         return Response(
#             status=status.HTTP_200_OK,
#             data=data
#         )
#     elif request.method == 'PUT':
#         serializer = ProductValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
#         product.title = serializer.validated_data.get('title')
#         product.description = serializer.validated_data.get('description')
#         product.category_id = serializer.validated_data.get('category_id')
#         product.save()
#         return Response(status=status.HTTP_201_CREATED, data = ProductListSerializer(product).data)
#     elif request.method == 'DELETE':
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def review_list_api_view(request):
#     if request.method == 'GET':
#         reviews = Review.objects.all()
#         data = ReviewListSerializer(instance=reviews, many=True).data
#         return Response(
#             status=status.HTTP_200_OK,
#             data=data
#         )
#     elif request.method == 'POST':
#         serializer = ReviewValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
#         text = serializer.validated_data.get('text')
#         product_id = serializer.validated_data.get('product_id')
#         stars = serializer.validated_data.get('stars')
#         review = Review.objects.create(
#             text=text,
#             product_id=product_id,
#             stars=stars
#         )
#         return Response(status=status.HTTP_201_CREATED, data=ReviewListSerializer(review).data)


# @api_view(['GET', 'PUT', 'DELETE'])
# def review_detail_api_view(request, id):
#     review = get_object_or_404(Review, id=id)
#     if request.method == 'GET':
#         data = ReviewListSerializer(instance=review, many=False).data
#         return Response(
#             status=status.HTTP_200_OK,
#             data=data
#         )
#     elif request.method == 'PUT':
#         serializer = ReviewValidateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
#         review.text = serializer.validated_data.get('text')
#         review.product_id = serializer.validated_data.get('product_id')
#         review.stars = serializer.validated_data.get('stars')
#         review.save()
#         return Response(status=status.HTTP_201_CREATED, data = ReviewListSerializer(review).data)
#     elif request.method == 'DELETE':
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)