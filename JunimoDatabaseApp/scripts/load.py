import csv
import os
from ..models.resource import Resource

def run():
    file = open('JunimoDatabaseApp/scripts/resources.csv')
    read_file=csv.reader(file)

    #optional - clears database of existing values
    Resource.objects.all().delete()

    #to avoid header values being added in accidentally
    count = 1 

    # add in resources from csv
    for resource in read_file:
        if count==1:
            pass
        else:
            print(resource) #optional
            Resource.objects.create(resource_name=resource[0], resource_description=resource[1], resource_image=resource[2], sale_price=resource[3], link_to_wiki=resource[4])
        count=count+1