from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    published_date = models.DateField()
    is_available = models.BooleanField(default=True)

    def _str_(self):
        return self.title