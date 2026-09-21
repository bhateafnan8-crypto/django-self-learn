from django.db import models

# Create your models here.

# simple ModelForm
class Invoice(models.Model):
    name = models.CharField(max_length=50)
    inv_id = models.CharField()
    amount = models.DecimalField(max_digits=10,decimal_places=2)

# Object creation, ModelForm
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=200)
    rating = models.IntegerField(max_length=5, default=False)