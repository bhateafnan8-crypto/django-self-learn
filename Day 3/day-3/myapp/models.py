from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name if self.name else "Unknown product"
    
class User(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    is_paid = models.BooleanField(default=False)
    date_of_purchase = models.DateField(auto_now_add=True)