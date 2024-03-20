from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField('Recipe name', max_length=100)
    link = models.CharField('Recipe link',max_length=200)
    cuisine = models.CharField('Recipe cuisine',max_length=100)
    diet = models.CharField('Recipe diet',max_length=100, null=True)
    prep_time = models.CharField('Recipe time',max_length=5)
    keywords = models.CharField('Recipe keyword',max_length=300)

    def __str__(self):
        return self.name

