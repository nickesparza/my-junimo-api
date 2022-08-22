from django.db import models

# Create your models here.
class Blueprint(models.Model):
    recipe_name = models.CharField(max_length=50)
    recipe_description = models.CharField(max_length=500)
    image = models.CharField(max_length=150)
    processor_needed = models.CharField(max_length=50)
    link_to_wiki = models.CharField(max_length=150)

    def __str__(self):
        return self.recipe_name

