from django.db import models

from JunimoDatabaseApp.models.character import Character
from JunimoDatabaseApp.models.material import Material

# you will need to bring over the user for authentication
# do we want to create an amount of 0 for all resource IDs?

# Create your models here.
class Inventory(models.Model):
    character_id = models.ForeignKey(Character, on_delete=models.CASCADE)
    material_id = models.ForeignKey(Material, on_delete=models.CASCADE)
    amount = models.IntegerField()
    def __str__(self):
        return ("{}'s {}".format(self.character_id, self.material_id) )


# if update amount, all that is needed to send is character id, resource id, new amount