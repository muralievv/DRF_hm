from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('categories', views.CategoryViewSet)
router.register('products', views.ProductViewSet)
router.register('reviews', views.ReviewViewSet)

urlpatterns = [
   path('', include(router.urls)),
]