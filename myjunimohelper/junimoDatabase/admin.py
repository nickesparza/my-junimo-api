from django.contrib import admin

# Register your models here.
from .models import Character
from .models import Resource
from .models import Blueprint
from .models import Inventory
from .models import RecipeMaterial
# Register your models here.

# this associates the admin with the Other models
admin.site.register(Character)
admin.site.register(Resource)
admin.site.register(Blueprint)
admin.site.register(Inventory)
admin.site.register(RecipeMaterial)