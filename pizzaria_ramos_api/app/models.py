from django.db import models

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=60)
    ingredients = models.TextField()
    price = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)

    # TODO: add field for uploaded image

