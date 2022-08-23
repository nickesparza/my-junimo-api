import csv
import os
from ..models.blueprint import Blueprint

def run():
    file = open('JunimoDatabaseApp/scripts/blueprints.csv')
    read_file=csv.reader(file)

    #optional - clears database of existing values
    Blueprint.objects.all().delete()

    #to avoid header values being added in accidentally
    count = 1 

    # add in resources from csv
    for blueprint in read_file:
        if count==1:
            pass
        else:
            print(blueprint) #optional
            Blueprint.objects.create(recipe_name=blueprint[0], recipe_description=blueprint[1], recipe_image=blueprint[2], processor_needed=blueprint[3], link_to_wiki=blueprint[4])
        count=count+1