from django.db import models # db module

# Create your models here.

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=200)
    ingredients = models.TextField() 
    is_vegetarian = models.BooleanField(default=False)
    photo_path = models.TextField(max_length=200)
    
    def __str__(self):
        return self.recipe_name + str(self.is_vegetarian)
