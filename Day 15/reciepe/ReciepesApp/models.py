from django.db import models

# Create your models here.

class RecipesModel(models.Model):
    reciepe_name = models.CharField()
    reciepe_description = models.TextField()
    reciepe_image = models.ImageField(upload_to='reciepe_images')
    