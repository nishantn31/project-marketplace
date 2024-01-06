from django.db import models
from django.contrib.auth.models import User
from myapp.utils import generate_slug

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    icon = models.CharField(max_length=50, blank=True)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

condition_choices = (
    ("Excellent","Excellent"),
    ("Very Good", "Very Good"),
    ("Average", "Average"),
    ("Bad", "Bad"),
    ("Poor","Poor"),)

class Product(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.FloatField()
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    condition = models.CharField(max_length = 20, choices = condition_choices)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    brand = models.CharField(max_length=200)
    

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(Product, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural="Product Table"


class ProductImage(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to="products/%Y/%m/%d")


class BuyerPrice(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    price = models.FloatField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.buyer

