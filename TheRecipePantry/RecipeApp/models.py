from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    cuisine = models.CharField(max_length=100)
    diet = models.CharField(max_length=100, null=True)
    prep_time = models.CharField(max_length=5)
    keywords = models.CharField(max_length=300)
