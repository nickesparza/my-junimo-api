import csv
import os
from ..models.recipe_material import RecipeMaterial

def run():
    file = open('JunimoDatabaseApp/scripts/recipematerial.csv')
    read_file=csv.reader(file)

    #optional - clears database of existing values
    RecipeMaterial.objects.all().delete()

    #to avoid header values being added in accidentally
    count = 1 

    # add in resources from csv
    for recipematerial in read_file:
        if count==1:
            pass
        else:
            print(recipematerial) #optional
            RecipeMaterial.objects.create(resource_id=recipematerial[0], blueprint_id=recipematerial[1], amount_needed=recipematerial[2])
        count=count+1