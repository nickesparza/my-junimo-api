from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from JunimoDatabaseApp.models import Resource

from ..serializers import ResourceSerializer

# Create your views here.
class Resources(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = ResourceSerializer
    def get(self, request):
        """Index request"""
        # Get all the characters:
        # characters = Character.objects.all()
        # Filter the characters by owner, so you can only see your owned characters
        resources = Resource.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = ResourceSerializer(resources, many=True).data
        return Response({ 'characters': data })

# don't need to post!
    # def post(self, request):
    #     """Create request"""
    #     # Serialize/create resource
    #     resource = ResourceSerializer(data=request.data['resource'])
    #     # If the resource data is valid according to our serializer...
    #     if resource.is_valid():
    #         # Save the created resource & send a response
    #         resource.save()
    #         return Response({ 'resource': resource.data }, status=status.HTTP_201_CREATED)
    #     # If the data is not valid, return a response with the errors
    #     return Response(resource.errors, status=status.HTTP_400_BAD_REQUEST)

class ResourceDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the resource to show
        resource = get_object_or_404(Resource, pk=pk)

        # Run the data through the serializer so it's formatted
        data = ResourceSerializer(resource).data
        return Response({ 'resource': data })

# don't need to delete!
    # def delete(self, request, pk):
    #     """Delete request"""
    #     # Locate resource to delete
    #     character = get_object_or_404(Character, pk=pk)
    #     # Check the mango's owner against the user making this request
    #     if request.user != character.owner:
    #         raise PermissionDenied('Unauthorized, you do not own this character')
    #     # Only delete if the user owns the character
    #     character.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


# don't need to update
    # def partial_update(self, request, pk):
    #     """Update Request"""
    #     # Locate Character
    #     # get_object_or_404 returns a object representation of our Character
    #     character = get_object_or_404(Character, pk=pk)
    #     # Check the character's owner against the user making this request
    #     if request.user != character.owner:
    #         raise PermissionDenied('Unauthorized, you do not own this character')

    #     # Ensure the owner field is set to the current user's ID
    #     request.data['character']['owner'] = request.user.id
    #     # Validate updates with serializer
    #     data = CharacterSerializer(character, data=request.data['character'], partial=True)
    #     if data.is_valid():
    #         # Save & send a 204 no content
    #         data.save()
    #         return Response(status=status.HTTP_204_NO_CONTENT)
    #     # If the data is not valid, return a response with the errors
    #     return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
