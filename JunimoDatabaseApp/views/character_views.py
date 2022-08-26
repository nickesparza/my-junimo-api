from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.db import models

from ..models.character import Character
from ..models.inventory import Inventory
from ..serializers import CharacterSerializer, InventorySerializer




# Create your views here.
class Characters(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = CharacterSerializer

    def get(self, request):
        """Index request"""
        # Filter the characters by owner, so you can only see your owned characters
        characters = Character.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = CharacterSerializer(characters, many=True).data
        return Response({ 'characters': data })

    # # def create_inventory(self, request):
    # #     # use this to seed the inventory upon character creation
    #     inventory = InventorySerializer(1, char_id, 0)
    # #     return Response({ 'inventory': inventory.data }, status=status.HTTP_201_CREATED)

        
    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['character']['owner'] = request.user.id
        # Serialize/create character
        character = CharacterSerializer(data=request.data['character'])
        # If the character data is valid according to our serializer...
        if character.is_valid():
            # Save the created character & send a response
            saved_character = character.save()
            print(saved_character.pk)
            # this returns the primary key of the newly created character
            char_id = saved_character.pk
            #######################
            # we will handle "creating" amount = 0 instances of inventory_materials for 
            # characters ON THE FRONT END
            #######################
            return Response({ 'character': character.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(character.errors, status=status.HTTP_400_BAD_REQUEST)



class CharacterDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the character to show
        character = get_object_or_404(Character, pk=pk)
        # Only want to show owned characters?
        if request.user != character.owner:
            raise PermissionDenied('Unauthorized, you do not own this character')

        # Run the data through the serializer so it's formatted
        data = CharacterSerializer(character).data
        return Response({ 'character': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate character to delete
        character = get_object_or_404(Character, pk=pk)
        # Check the characters's owner against the user making this request
        if request.user != character.owner:
            raise PermissionDenied('Unauthorized, you do not own this character')
        # Only delete if the user owns the character
        character.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate Character
        # get_object_or_404 returns a object representation of our Character
        character = get_object_or_404(Character, pk=pk)
        # Check the character's owner against the user making this request
        if request.user != character.owner:
            raise PermissionDenied('Unauthorized, you do not own this character')

        # Ensure the owner field is set to the current user's ID
        request.data['character']['owner'] = request.user.id
        # Validate updates with serializer
        data = CharacterSerializer(character, data=request.data['character'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
