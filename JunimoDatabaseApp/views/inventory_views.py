from webbrowser import get
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
# from JunimoDatabaseApp.models import character
from ..models.character import Character
from ..models.material import Material
from ..models.inventory import Inventory
from ..serializers import CharacterSerializer
from ..serializers import InventorySerializer, UpdateInventorySerializer

# We will not need an inventory index page 

# Create your views here.

# this will affect ONE inventory entry for ONE character
class ShowInventoryView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
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

    # THESE ARE TRICKY DUE TO NESTED DATA
    # create an entry in inventory
    def post(self, request, pk, fk):
        # this would work for patch better
        """Create request"""
        # Filter the characters by owner, so you can only see your owned characters
        character = get_object_or_404(Character, pk=fk)
        # Only do request if they own the character whose inventory it is
        if request.user != character.owner:
            raise PermissionDenied('Unauthorized, you do not own this character')
        # Only do request if they own the character whose inventory it is
        if request.user != character.owner:
            raise PermissionDenied('Unauthorized, you do not own this character')
            # If pass...
        # print the request data
        print(request.data)
        # Serialize/create inventory
        inventory = UpdateInventorySerializer(data=request.data)
        # If the inventory data is valid according to our serializer...
        if inventory.is_valid():
            # Save the created inventory & send a response
            inventory.save()
            return Response({ 'inventory': inventory.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(inventory.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, pk, fk):
        """Update Request"""
        # Locate Character for auth
        character = get_object_or_404(Character, pk=fk)
        # Check the character's owner against the user making this request
        if request.user != character.owner:
            raise PermissionDenied('Unauthorized, you do not own this character')
            # If pass...    
        inventory = get_object_or_404(Inventory, pk=pk)
        # Serialize/create inventory for validation
        # Validate updates with serializer
        updated_inventory = UpdateInventorySerializer(inventory, data=request.data)
        if updated_inventory.is_valid():
            # Save & send a 204 no content
            updated_inventory.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(updated_inventory.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, fk):
        """Delete request"""
        # Locate mango to delete
        character = get_object_or_404(Character, pk=pk)
        # Check the characters's owner against the user making this request
        if request.user != character.owner:
            raise PermissionDenied('Unauthorized, you do not own this character')
        # Only delete if the user owns the character
        # set inventory to delete
        inventory = get_object_or_404(Inventory, pk=fk)
        inventory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# this returns an index for all inventory items connected to ONE CHARACTER
class InventoryDetail(generics.ListCreateAPIView):
    serializer_class = InventorySerializer
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

    
