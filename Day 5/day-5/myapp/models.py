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
    rating = models.IntegerField(default=0)


class Job(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    cgpa = models.DecimalField(max_digits=5,decimal_places=2)
    experience = models.CharField(max_length=50)

class Student(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(
        upload_to="students/"
    )