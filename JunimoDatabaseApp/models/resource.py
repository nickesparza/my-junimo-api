from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Resource(models.Model):
    resource_name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    image = models.CharField(max_length=150)
    sale_price = models.IntegerField(
        validators=[
            MaxValueValidator(2147483647),
            MinValueValidator(1),
        ]
    )
    link_to_wiki = models.CharField(max_length=150)
    def __str__(self):
        return self.resource_name

