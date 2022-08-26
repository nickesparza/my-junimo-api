from django.db import models
from rest_framework import generics, status
from rest_framework.response import Response
# from ..views.character_views import char_id

from JunimoDatabaseApp.models.character import Character
from JunimoDatabaseApp.models.material import Material
# from ..serializers import UpdateInventorySerializer

# you will need to bring over the user for authentication
# do we want to create an amount of 0 for all resource IDs?

# Create your models here.
class Inventory(models.Model):
    character_id = models.ForeignKey(Character, on_delete=models.CASCADE)
    material_id = models.ForeignKey(Material, on_delete=models.CASCADE)
    amount = models.IntegerField()
    def __str__(self):
        return ("{}'s {}".format(self.character_id, self.material_id) )

    # def create(char_id):
    #     # use this to seed the inventory upon character creation
    #     inventory = UpdateInventorySerializer(data=char_id)
    #     # If the inventory data is valid according to our serializer...
    #     if inventory.is_valid():
    #         # Save the created inventory & send a response
    #         inventory.save()
    #         return Response({ 'inventory': inventory.data }, status=status.HTTP_201_CREATED)
    #     return inventory


# if update amount, all that is needed to send is character id, resource id, new amount