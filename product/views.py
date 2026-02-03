from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Category, Review
from .serializers import CategoryListSerializer, ProductListSerializer, ReviewListSerializer


@api_view(['GET', 'POST'])
def categories_list_api_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        data = CategoryListSerializer(instance=categories, many=True).data
        return Response(
            status=status.HTTP_200_OK,
            data=data
        )
    elif request.method == 'POST':
        name = request.data.get('name')
        category = Category.objects.create(
            name=name
        )
        return Response(status=status.HTTP_201_CREATED,
        data=CategoryListSerializer(category).data)
        

@api_view(['GET', 'PUT','DELETE'])
def category_detail_api_view(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'GET':
        data = CategoryListSerializer(instance=category, many=False).data
        return Response(
            status=status.HTTP_200_OK,
            data=data
        )
    elif request.method == 'PUT':
        category.name = request.data.get('name')
        category.save()
        return Response(status=status.HTTP_201_CREATED, data = CategoryListSerializer(category).data)
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def product_list_api_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        data = ProductListSerializer(instance=products, many=True).data
        return Response(
            status=status.HTTP_200_OK,
            data=data
        )
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        category_id = request.data.get('category_id')
        product = Product.objects.create(
            title=title,
            description=description,
            category_id=category_id
        )
        return Response(status=status.HTTP_201_CREATED,
                        data=ProductListSerializer(product).data)

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'GET':
        data = ProductListSerializer(instance=product, many=False).data
        return Response(
            status=status.HTTP_200_OK,
            data=data
        )
    elif request.method == 'PUT':
        product.title = request.data.get('title')
        product.description = request.data.get('description')
        product.categoty_id = request.data.get('category_id')
        product.save()
        return Response(status=status.HTTP_201_CREATED, data = ProductListSerializer(product).data)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        data = ReviewListSerializer(instance=reviews, many=True).data
        return Response(
            status=status.HTTP_200_OK,
            data=data
        )
    elif request.method == 'POST':
        text = request.data.get('text')
        product_id = request.data.get('product_id')
        stars = request.data.get('stars')
        review = Review.objects.create(
            text=text,
            product_id=product_id,
            stars=stars
        )
        return Response(status=status.HTTP_201_CREATED, data=ReviewListSerializer(review).data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    review = get_object_or_404(Review, id=id)
    if request.method == 'GET':
        data = ReviewListSerializer(instance=review, many=False).data
        return Response(
            status=status.HTTP_200_OK,
            data=data
        )
    elif request.method == 'PUT':
        review.text = request.data.get('text')
        review.product_id = request.data.get('product_id')
        review.stars = request.data.get('stars')
        review.save()
        return Response(status=status.HTTP_201_CREATED, data = ReviewListSerializer(review).data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)