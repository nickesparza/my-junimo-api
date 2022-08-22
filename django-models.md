<!-- * Characters Table - (one to many from user to characters; 'saves') (fully crudable) 
    - Name (string)
    - Platform (string)
    - Farm Type (string)
    - Pet Type (string)
    - Pet Name (string)
    - Pet image (if cat, choose cat images; if dog, choose dog images - are there pigs too?) (string)
    - Love Interest/Spouse (string)
    - Horse Name (string)
    - Total G
    - Year  -->


class Character(models.Model):
    CAT = 'cat'
    DOG = 'dog'
    PET_TYPE_CHOICES = [
        (CAT, 'Cat'),
        (DOG, 'Dog'),
    ]
    name = models.CharField(max_length=12)
    Platform = models.CharField(max_length=30)
    farm_name = models.CharField(max_length=12)
    # this lets us define the choices given the character
    pet_type = models.CharField(
        max_length=3,
        choices=PET_TYPE_CHOICES,
        default=CAT,
    )
    pet_name = models.CharField(max_length=12)
    pet_image = 
    love_interest = 
    horse_name = models.CharField(max_length=12)
    total_g = models.IntegerField()
    year = models.IntegerField()