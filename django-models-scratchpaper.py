# * Characters Table - (one to many from user to characters; 'saves') (fully crudable) 
#     - Name (string)
#     - Platform (string)
#     - Farm Type (string)
#     - Pet Type (string)
#     - Pet Name (string)
#     - Pet image (if cat, choose cat images; if dog, choose dog images - are there pigs too?) (string)
#     - Love Interest/Spouse (string)
#     - Horse Name (string)
#     - Total G
#     - Year 

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Character(models.Model):
    # we will use these constants for the pets later on
    CAT = 'cat',
    DOG = 'dog',
    # this defines the pet choices later on
    PET_TYPE_CHOICES = [
        (CAT, 'Cat'),
        (DOG, 'Dog'),
    ]
    # we will use these constants for the love interests! yes I will be adding in Krobus
    ALEX = 'AL',
    ELLIOT = 'EL',
    HARVEY = 'HA',
    SAM = 'SA',
    SEBASTIAN = 'SE',
    SHANE = 'SH',
    ABIGAIL = 'AB',
    EMILY = 'EM',
    HALEY = 'HL',
    LEAH = 'LE',
    MARU = 'MA',
    PENNY = 'PE',
    KROBUS = 'KR',
    # this defines the love interest choices later on
    LOVE_INTEREST_CHOICES = [
        (ALEX, 'Alex'),
        (ELLIOT, 'Elliot'),
        (HARVEY, 'Harvey'),
        (SAM, 'Sam'),
        (SEBASTIAN, 'Sebastian'),
        (SHANE, 'Shane'),
        (ABIGAIL, 'Abigail'),
        (EMILY, 'Emily'),
        (HALEY, 'Haley'),
        (LEAH, 'Leah'),
        (MARU, 'Maru'),
        (PENNY, 'Penny'),
        (KROBUS, 'Krobus'),
    ]
    # this defines the pet choices later on
    PET_TYPE_CHOICES = [
        (CAT, 'Cat'),
        (DOG, 'Dog'),
    ]
    # and these are for the pet urls
    CAT1 = 'C1',
    CAT2 = 'C2',
    CAT3 = 'C3',
    DOG1 = 'D1',
    DOG2 = 'D2',
    DOG3 = 'D3',
    # this defines the pet URL choices later on
    PET_URL_CHOICES = [
        (CAT1, 'Cat 1'),
        (CAT2, 'Cat 2'),
        (CAT3, 'Cat 2'),
        (DOG1, 'Dog 1'),
        (DOG2, 'Dog 2'),
        (DOG3, 'Dog 3'),
    ]
    # and now for the models
    name = models.CharField(max_length=12)
    Platform = models.CharField(max_length=30)
    farm_name = models.CharField(max_length=12)
    # this lets us define the choices given the character
    pet_type = models.CharField(
        max_length=3,
        choices=PET_TYPE_CHOICES,
    )
    pet_name = models.CharField(max_length=12)
    pet_image = models.CharField(
        max_length=2,
        choices=PET_URL_CHOICES,
    )
    love_interest = models.CharField(
        max_length=2,
        choices=LOVE_INTEREST_CHOICES,
    )
    horse_name = models.CharField(max_length=12)
    total_g = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(2147483647),
            MinValueValidator(1),
        ]
    )
    year = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(1000),
            MinValueValidator(1),
        ]
    )


# * Materials Table
#     - material name
#     - description
#     - image
#     - sale price
#     - link to wiki page

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

# * Crafting Recipes Table
#     - name
#     - description
#     - processor needed (eg. forge, kiln)

#Given a model instance, the display value for a field with choices can be accessed using the get_FOO_display() method. 

class Blueprint(models.Model):
    recipe_name = models.CharField(max_length=50)
    recipe_description = models.CharField(max_length=500)
    image = models.CharField(max_length=150)
    processor_needed = models.CharField(max_length=50)
    link_to_wiki = models.CharField(max_length=150)

class Inventory(models.Model):


class RecipeMaterials(models.Model):
    