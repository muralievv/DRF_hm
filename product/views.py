from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Category, Review
from .serializers import CategoryListSerializer, ProductListSerializer, ReviewListSerializer


@api_view(['GET'])
def categories_list_api_view(request):
    categories = Category.objects.all()
    data = CategoryListSerializer(instance=categories, many=True).data
    return Response(
        status=status.HTTP_200_OK,
        data=data
    )

@api_view(['GET'])
def category_detail_api_view(request, id):
    category = get_object_or_404(Category, id=id)
    data = CategoryListSerializer(instance=category, many=False).data
    return Response(
        status=status.HTTP_200_OK,
        data=data
    )
@api_view(['GET'])
def product_list_api_view(request):
    products = Product.objects.all()
    data = ProductListSerializer(instance=products, many=True).data
    return Response(
        status=status.HTTP_200_OK,
        data=data
    )

@api_view(['GET'])
def product_detail_api_view(request, id):
    product = get_object_or_404(Product, id=id)
    data = ProductListSerializer(instance=product, many=False).data
    return Response(
        status=status.HTTP_200_OK,
        data=data
    )

@api_view(['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    data = ReviewListSerializer(instance=reviews, many=True).data
    return Response(
        status=status.HTTP_200_OK,
        data=data
    )

@api_view(['GET'])
def review_detail_api_view(request, id):
    review = get_object_or_404(Review, id=id)
    data = ReviewListSerializer(instance=review, many=False).data
    return Response(
        status=status.HTTP_200_OK,
        data=data
    )