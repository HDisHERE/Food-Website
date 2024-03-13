from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    cuisine = models.CharField(max_length=100)
    diet = models.CharField(max_length=100)
    prep_tim = models.TimeField(auto_now=False, auto_now_add=False)
    keywords = models.CharField(max_length=300)
