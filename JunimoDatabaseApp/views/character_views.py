from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.db import models

from ..models.character import Character
# from ..models.inventory import Inventory, create
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

    # def seed_inventory(self, request):
    #     # use this to seed the inventory upon character creation
    #     inventory = InventorySerializer(request.data)
    #     return Response({ 'inventory': inventory.data }, status=status.HTTP_201_CREATED)

        
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
            # # IF WE WANT TO AUTOMATICALLY CREATE SEVERAL AMOUNT=0 INSTANCES OF INVENTORY ATTACHED TO THIS NEWLY CREATED CHARACTER...
            # # HERE IS WHERE IT GOES (USING POST.SAVE?)
            # inventory_entries = [
            #     Inventory(1, char_id, 0),
            #     Inventory(2, char_id, 0),
            #     Inventory(3, char_id, 0),
            #     Inventory(4, char_id, 0),
            #     Inventory(5, char_id, 0),
            #     Inventory(6, char_id, 0),
            #     Inventory(7, char_id, 0),
            #     Inventory(8, char_id, 0),
            #     Inventory(9, char_id, 0),
            #     Inventory(10, char_id, 0),
            #     Inventory(11, char_id, 0),
            #     Inventory(12, char_id, 0),
            #     Inventory(13, char_id, 0),
            #     Inventory(14, char_id, 0),
            #     Inventory(15, char_id, 0),
            #     Inventory(16, char_id, 0),
            #     Inventory(17, char_id, 0),
            #     Inventory(18, char_id, 0),
            #     Inventory(19, char_id, 0),
            #     Inventory(20, char_id, 0),
            #     Inventory(21, char_id, 0),
            #     Inventory(22, char_id, 0),
            #     Inventory(23, char_id, 0),
            #     Inventory(24, char_id, 0),
            #     Inventory(25, char_id, 0),
            #     Inventory(26, char_id, 0),
            #     Inventory(27, char_id, 0),
            #     Inventory(28, char_id, 0),
            #     Inventory(29, char_id, 0),
            #     Inventory(30, char_id, 0),
            #     Inventory(31, char_id, 0),
            #     Inventory(32, char_id, 0),
            #     Inventory(33, char_id, 0),
            #     Inventory(34, char_id, 0),
            #     Inventory(35, char_id, 0),
            #     Inventory(36, char_id, 0),
            #     Inventory(37, char_id, 0),
            #     Inventory(38, char_id, 0),
            #     Inventory(39, char_id, 0),
            #     Inventory(40, char_id, 0),
            #     Inventory(41, char_id, 0),
            #     Inventory(42, char_id, 0),
            #     Inventory(43, char_id, 0),
            #     Inventory(44, char_id, 0),
            #     Inventory(45, char_id, 0),
            #     Inventory(46, char_id, 0),
            #     Inventory(47, char_id, 0),
            #     Inventory(48, char_id, 0),
            #     Inventory(49, char_id, 0),
            #     Inventory(50, char_id, 0),
            #     Inventory(51, char_id, 0),
            #     Inventory(52, char_id, 0),
            #     Inventory(53, char_id, 0),
            #     Inventory(54, char_id, 0),
            #     Inventory(55, char_id, 0),
            #     Inventory(56, char_id, 0),
            #     Inventory(57, char_id, 0),
            #     Inventory(58, char_id, 0),
            #     Inventory(59, char_id, 0),
            #     Inventory(60, char_id, 0),
            #     Inventory(61, char_id, 0),
            #     Inventory(62, char_id, 0),
            #     Inventory(63, char_id, 0),
            #     Inventory(64, char_id, 0),
            #     Inventory(65, char_id, 0),
            #     Inventory(66, char_id, 0),
            #     Inventory(67, char_id, 0),
            #     Inventory(68, char_id, 0),
            #     Inventory(69, char_id, 0),
            #     Inventory(70, char_id, 0),
            #     Inventory(71, char_id, 0),
            #     Inventory(72, char_id, 0),
            #     Inventory(73, char_id, 0),
            #     Inventory(74, char_id, 0),
            #     Inventory(75, char_id, 0),
            #     Inventory(76, char_id, 0),
            #     Inventory(77, char_id, 0),
            #     Inventory(78, char_id, 0),
            #     Inventory(79, char_id, 0),
            #     Inventory(80, char_id, 0),
            # ]
            # Inventory.create(inventory_entries)
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
