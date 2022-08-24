import csv
import os
from ..models.material import Material

def run():
    file = open('JunimoDatabaseApp/scripts/resources.csv')
    read_file=csv.reader(file)

    #optional - clears database of existing values
    Material.objects.all().delete()

    #to avoid header values being added in accidentally
    count = 1 

    # add in resources from csv
    for material in read_file:
        if count==1:
            pass
        else:
            print(material) #optional
            Material.objects.create(material_name=material[0], material_description=material[1], material_image=material[2], sale_price=material[3], link_to_wiki=material[4])
        count=count+1