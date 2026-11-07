from django.db import models

# Create your models here.

class RecipesModel(models.Model):
    reciepe_name = models.CharField()
    reciepe_desc = models.TextField()
    reciepe_img = models.ImageField(upload_to='reciepe_images')
    