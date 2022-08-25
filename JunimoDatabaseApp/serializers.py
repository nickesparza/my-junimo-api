from ast import Pass
from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models.character import Character
from .models.material import Material
from .models.blueprint import Blueprint
from .models.inventory import Inventory
from .models.recipe_material import RecipeMaterial
from .models.user import User


# class MangoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Mango
#         fields = ('id', 'name', 'color', 'ripe', 'owner')

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'

class BlueprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blueprint
        fields = '__all__'

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'


# for serializer SPECIFICALLY for GET routes (read only)
# character name, character id, resource name, resource id, resource image, amount
class InventorySerializer(serializers.ModelSerializer):
    material = MaterialSerializer(source='material_id', read_only=True)
    character = CharacterSerializer(source='character_id', read_only=True)
    class Meta:
        model = Inventory
        fields = ('material', 'character', 'amount', 'id')
        # this sets the 'nested' fields above as read only
        extra_kwargs = {
            'material': {
                'read_only': True
            },
            'character': {
                'read_only': True
            }
        }



# # if the issue is that the InventorySerializer is expecting more fields, do we need that? 
# # Can we make a simpler serializer SPECIFICALLY for post/patch?
# for serializer SPECIFICALLY for PATCH/POST routes
class UpdateInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('__all__')
        
    # def create(self, validated_data):
    #     material_validated_data = validated_data.pop('material')
    #     character_validated_data = validated_data.pop('character')
    #     amount_validated_data = validated_data.pop('amount')
    #     inventory = Inventory.objects.create(**validated_data)
    #     return inventory

    # def update(self, instance, validated_data):
    #     material_validated_data = validated_data.pop('material')
    #     character_validated_data = validated_data.pop('character')
    #     amount_validated_data = validated_data.pop('amount')
    #     # instance.material_id = validated_data.get('material_id', instance.material_id)
    #     # instance.character_id = validated_data.get('character_id', instance.character_id)
    #     instance.material = validated_data.get('material', instance.material)
    #     instance.character = validated_data.get('character', instance.character)
    #     instance.amount = validated_data.get('amount', instance.amount)
    #     instance.save()
    #     return instance

class RecipeMaterialSerializer(serializers.ModelSerializer):
    material = MaterialSerializer(source='material_id')
    blueprint = BlueprintSerializer(source='blueprint_id')
    class Meta:
        model = RecipeMaterial
        fields = ('material', 'blueprint', 'amount_needed', 'id')
        # this sets the 'nested' fields above as read only
        extra_kwargs = {
            'material': {
                'read_only': True
            },
            'blueprint': {
                'read_only': True
            }
        }


class UserSerializer(serializers.ModelSerializer):
    # This model serializer will be used for User creation
    # The login serializer also inherits from this serializer
    # in order to require certain data for login
    class Meta:
        # get_user_model will get the user model (this is required)
        # https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#referencing-the-user-model
        model = get_user_model()
        fields = ('id', 'email', 'password')
        extra_kwargs = { 'password': { 'write_only': True, 'min_length': 5 } }

    # This create method will be used for model creation
    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

class UserRegisterSerializer(serializers.Serializer):
    # Require email, password, and password_confirmation for sign up
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True)
    password_confirmation = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        # Ensure password & password_confirmation exist
        if not data['password'] or not data['password_confirmation']:
            raise serializers.ValidationError('Please include a password and password confirmation.')

        # Ensure password & password_confirmation match
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError('Please make sure your passwords match.')
        # if all is well, return the data
        return data

class ChangePasswordSerializer(serializers.Serializer):
    model = get_user_model()
    old = serializers.CharField(required=True)
    new = serializers.CharField(required=True)
