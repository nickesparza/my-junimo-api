from django.db import models
from models import Blueprint, Resource

# Create your models here.
class RecipeMaterial(models.Model):
    resource_id = models.ForeignKey(Resource, on_delete=models.CASCADE)
    blueprint_id = models.ForeignKey(Blueprint, on_delete=models.CASCADE)
    amount_needed = models.IntegerField()
    
    def __str__(self):
        return ("{} for {}".format(self.resource_id, self.blueprint_id) )

