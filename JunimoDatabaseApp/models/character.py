from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Character(models.Model):
    # define fields
    # https://docs.djangoproject.com/en/3.0/ref/models/fields/
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    # we will use these constants for the pets later on
    CAT = 'Cat'
    DOG = 'Dog'
    # this defines the pet choices later on
    PET_TYPE_CHOICES = [
        (CAT, 'Cat'),
        (DOG, 'Dog'),
    ]
    # we will use these constants for the love interests! yes I will be adding in Krobus
    ALEX = 'AL'
    ELLIOT = 'EL'
    HARVEY = 'HA'
    SAM = 'SA'
    SEBASTIAN = 'SE'
    SHANE = 'SH'
    ABIGAIL = 'AB'
    EMILY = 'EM'
    HALEY = 'HL'
    LEAH = 'LE'
    MARU = 'MA'
    PENNY = 'PE'
    KROBUS = 'KR'
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
    CAT1 = 'C1'
    CAT2 = 'C2'
    CAT3 = 'C3'
    DOG1 = 'D1'
    DOG2 = 'D2'
    DOG3 = 'D3'
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
            MinValueValidator(0),
        ]
    )
    year = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(2147483647),
            MinValueValidator(1),
        ]
    )
    def __str__(self):
        return self.name

