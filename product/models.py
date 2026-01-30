from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    
    @property
    def products_count(self):
        return self.product_set.count()

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=300, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete= models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def average_rating(self):
        reviews = self.reviews.all()
        count = reviews.count()
        if count > 0:
            total_stars = sum([review.stars for review in reviews])
            return round(total_stars / count, 1) 
        
        return 0

class Review(models.Model):
    text = models.TextField(null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, related_name='reviews')
    stars = models.IntegerField(default=0, validators=[
        MinValueValidator(1),
        MaxValueValidator(5),
    ])
  

    def __str__(self):
        return self.text 

