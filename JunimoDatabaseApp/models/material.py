from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Material(models.Model):
    material_name = models.CharField(max_length=50)
    material_description = models.CharField(max_length=500)
    material_image = models.CharField(max_length=150)
    sale_price = models.IntegerField(
        validators=[
            MaxValueValidator(2147483647),
            MinValueValidator(1),
        ]
    )
    link_to_wiki = models.CharField(max_length=150)
    def __str__(self):
        return self.material_name