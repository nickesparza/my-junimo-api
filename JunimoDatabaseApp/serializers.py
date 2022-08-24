from ast import Pass
from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models.character import Character
from .models.material import Material
from .models.blueprint import Blueprint
from .models.inventory import Inventory
from .models.recipe_material import RecipeMaterial
from .models.user import User
from JunimoDatabaseApp.models import material

from JunimoDatabaseApp.models import inventory

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


# for serializer
# character name, character id, resource name, resource id, resource image, amount
class InventorySerializer(serializers.ModelSerializer):
    material = MaterialSerializer(source='material_id')
    character = CharacterSerializer(source='character_id')
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
    def create(self, validated_data):
        material_validated_data = validated_data.pop('material_id')
        character_validated_data = validated_data.pop('character_id')
        amount_validated_data = validated_data.pop('amount')
        print(validated_data)
        inventory = Inventory.objects.create(**validated_data)
        # choice_set_serializer = self.fields['choice_set']
        # for each in choice_validated_data:
        #     each['question'] = question
        # choices = choice_set_serializer.create(choice_validated_data)
        return inventory


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
