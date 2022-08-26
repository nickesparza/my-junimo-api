import csv
import os
from ..models.recipe_material import RecipeMaterial
from ..models.blueprint import Blueprint
from ..models.material import Material
from django.shortcuts import get_object_or_404

def run():
    file = open('JunimoDatabaseApp/scripts/recipe_materials.csv')
    read_file=csv.reader(file)

    #optional - clears database of existing values
    RecipeMaterial.objects.all().delete()

    #to avoid header values being added in accidentally
    count = 1 

    # add in resources from csv
    for blueprint_material in read_file:
        if count==1:
            pass
        else:
            print(blueprint_material) #optional
            RecipeMaterial.objects.create(blueprint_id=get_object_or_404(Blueprint, pk=blueprint_material[0]), material_id=get_object_or_404(Material, pk=blueprint_material[1]), amount_needed=blueprint_material[2])
        count=count+1