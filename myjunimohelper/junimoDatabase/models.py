from ast import Pass
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings
from rest_framework.authtoken.models import Token

# Create your models here.

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

class UserManager(BaseUserManager):
    """Manager for user profiles"""

    # The create_user method is passed:
    # self:      All methods in Python receive the class as the first argument
    # email:     Because we want to be able to log users in with email
    #            instead of username (Django's default behavior)
    # password:  The password has a default of None for validation purposes.
    #            This ensures the proper error is thrown if a password is
    #            not provided.
    # **extra_fields:  Just in case there are extra arguments passed.
    def create_user(self, email, password=None, **extra_fields):
        """Create a new user profile"""
        # Add a custom validation error
        if not email:
            raise ValueError('User must have an email address')

        # Create a user from the UserModel
        # Use the normalize_email method from the BaseUserManager to
        # normalize the domain of the email
        # We'll also unwind the extra fields.  Remember that two asterisk (**)
        # in Python refers to the extra keyword arguments that are passed into
        # a function (meaning these are key=value pairs).
        user = self.model(email=self.normalize_email(email), **extra_fields)

        # Use the set_password method to hash the password
        user.set_password(password)
        # Call save to save the user to the database
        user.save()

        # Always return the user!
        return user

    def create_superuser(self, email, password):
        """Create and save a new superuser with given details"""

        # Use the custom create_user method above to create
        # the user.
        user = self.create_user(email, password)

        # Add the required is_superuser and is_staff properties
        # which must be set to True for superusers
        user.is_superuser = True
        user.is_staff = True
        # Save the user to the database with the new properties
        user.save()

        # Always return the user!
        return user

# Inherit from AbstractBaseUser and PermissionsMixin:
class User(AbstractBaseUser, PermissionsMixin):
    """Database model for users"""
    # As with any Django models, we need to define the fields
    # for the model with the type and options:
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    # name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Any time we call User.objects (such as in objects.all() or objects.filter())
    # make sure to use the custom user manager we created.
    objects = UserManager()

    # Tell Django to use the email field as the unique identifier for the
    # user account instead of its built in behavior of using the username.
    USERNAME_FIELD = 'email'
    # This doesn't mean the field is required (that's defined above in the field options)
    # This refers to the fields that are prompted for when creating a superuser.
    # https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#django.contrib.auth.models.CustomUser.REQUIRED_FIELDS
    # REQUIRED_FIELDS = ['name']

    # Standard Python: We'll create a string representation so when
    # the class is output we'll get something meaningful.
    def __str__(self):
        """Return string representation of the user"""
        return self.email

    def get_auth_token(self):
        Token.objects.filter(user=self).delete()
        token = Token.objects.create(user=self)
        self.token = token.key
        self.save()
        return token.key

    def delete_token(self):
        Token.objects.filter(user=self).delete()
        self.token = None
        self.save()
        return self

class Character(models.Model):
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
            MaxValueValidator(2147483647),
            MinValueValidator(1),
        ]
    )
    def __str__(self):
        return self.name

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
    def __str__(self):
        return self.resource_name

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
    def __str__(self):
        return self.recipe_name

class Inventory(models.Model):
    character_id = models.ForeignKey(Character, on_delete=models.CASCADE)
    resource_id = models.ForeignKey(Resource, on_delete=models.CASCADE)
    amount = models.IntegerField()
    def __str__(self):
        return ("{}'s {}".format(self.character_id, self.resource_id) )


# class RecipeMaterials(models.Model):
#     resource_id = models.ForeignKey(Resource, on_delete=models.CASCADE)
#     blueprint_id = models.ForeignKey(Blueprint, on_delete=models.CASCADE)
#     amount_needed = models.IntegerField()
#     def __str__(self):
#         return self.name

class RecipeMaterial(models.Model):
    resource_id = models.ForeignKey(Resource, on_delete=models.CASCADE)
    blueprint_id = models.ForeignKey(Blueprint, on_delete=models.CASCADE)
    amount_needed = models.IntegerField()
    def __str__(self):
        return ("{} for {}".format(self.resource_id, self.blueprint_id) )

