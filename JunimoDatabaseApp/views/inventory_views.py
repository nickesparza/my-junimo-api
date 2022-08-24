from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
# from JunimoDatabaseApp.models import character
from ..models.character import Character
from ..models.inventory import Inventory
from ..serializers import CharacterSerializer
from ..serializers import InventorySerializer

# We will not need an inventory index page 

# Create your views here.

# this will return ONE inventory entry for ONE character
class ShowInventoryView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = InventorySerializer
    def get(self, request, pk, fk):
        """Index request"""
        # Filter the characters by owner, so you can only see your owned characters
        character = get_object_or_404(Character, pk=fk)
        # Only do request if they own the character whose inventory it is
        if request.user != character.owner:
            raise PermissionDenied('Unauthorized, you do not own this character')
        # Filter the inventories by character, so you can only see your owned inventories
        inventory = get_object_or_404(Inventory, pk=pk, character_id=fk)
        # Run the data through the serializer
        data = InventorySerializer(inventory).data
        return Response({ 'inventory': data })

# TODO: TEST THIS
# create an entry in inventory
    def post(self, request, pk, fk):
        # this would work for patch better
        """Create request"""
        # Get character that you will be adding inventory item to
        character = get_object_or_404(Character, pk=pk)
        # Only do request if they own the character whose inventory it is
        if request.user != character.owner:
            raise PermissionDenied('Unauthorized, you do not own this character')
            # If pass...
        # Add character_id to request data object
        # set inventory character_id
        request.data['inventory']['character_id'] = pk
        # set inventory material_id
        request.data['inventory']['material_id'] = fk
        # Serialize/create inventory
        inventory = InventorySerializer(data=request.data['inventory'])
        # If the inventory data is valid according to our serializer...
        if inventory.is_valid():
            # Save the created inventory & send a response
            inventory.save()
            return Response({ 'inventory': inventory.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(inventory.errors, status=status.HTTP_400_BAD_REQUEST)

        # TODO: GET THESE TWO SORTED - this should be moved up under (generics.RetrieveUpdateDestroyAPIView)
    def delete(self, request, pk):
        """Delete request"""
        # Locate mango to delete
        character = get_object_or_404(Character, pk=pk)
        # Check the characters's owner against the user making this request
        if request.user != character.owner:
            raise PermissionDenied('Unauthorized, you do not own this character')
        # Only delete if the user owns the character
        character.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # TODO: TO TEST
    def partial_update(self, request, pk, fk):
        """Update Request"""
        # Locate Character for auth
        # get_object_or_404 returns a object representation of our Character
        character = get_object_or_404(Character, pk=pk)
        # Check the character's owner against the user making this request
        if request.user != character.owner:
            raise PermissionDenied('Unauthorized, you do not own this character')
            # If pass...    
        # set inventory character_id (ref with pk)
        request.data['inventory']['character_id'] = pk
        # set inventory material_id (ref with fk)
        request.data['inventory']['material_id'] = fk
        # Serialize/create inventory for validation
        # Validate updates with serializer
        inventory = InventorySerializer(data=request.data['inventory'])
        if inventory.is_valid():
            # Save & send a 204 no content
            inventory.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(inventory.errors, status=status.HTTP_400_BAD_REQUEST)


# this returns an index for all inventory items conncected to ONE CHARACTER
class InventoryDetail(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the character to show
        character = get_object_or_404(Character, pk=pk)
        # Only want to show owned characters?
        if request.user != character.owner:
            raise PermissionDenied('Unauthorized, you do not own this character')
        # return data where inventory.character_id = pk
        inventory = Inventory.objects.filter(character_id=pk)
        # Run the data through the serializer so it's formatted
        data = InventorySerializer(inventory, many=True).data
        return Response({ 'inventory': data })

    
