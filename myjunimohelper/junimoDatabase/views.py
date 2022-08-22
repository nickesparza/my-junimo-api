from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import Character, Resource, Blueprint, Inventory, RecipeMaterials
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CharacterSerializer

# Create your views here.
class CharactersView(APIView):
    """Class for Index and Post"""
    def get(self, request):
        """Index Characters"""
        characters = Character.objects.all()
        data = CharacterSerializer(characters, many=True).data
        return Response(data)
    
    def post(self, request):
        """Create Character"""
        print(request.data)
        character = CharacterSerializer(data=request.data)
        if character.is_valid():
            character.save()
            return Response(character.data, status=status.HTTP_201_CREATED)
        else:
            return Response(character.errors, status=status.HTTP_400_BAD_REQUEST)

# non-serialized views
# def index(request):
#     characters = Character.objects.all()
#     data = list(characters.values())
#     return JsonResponse(data, safe=False)

# def character_show(request, character_id):
#     character = Character.objects.get(id=character_id)
#     data = list(character.values())
#     return JsonResponse(data, safe=False)

class CharacterDetailView(APIView):
    def get(self, request, pk):
        """Show one character"""
        character = get_object_or_404(Character, pk=pk)
        data = CharacterSerializer(character).data
        return Response(data)
    
    def delete(self, request, pk):
        """Deletes a character"""
        character = get_object_or_404(Character, pk=pk)
        character.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, pk):
        """Update a Character"""
        # first we locate the character
        character = get_object_or_404(Character, pk=pk)
        # then we run our update through the serializer
        updated_character = CharacterSerializer(character, data=request.data)
        if updated_character.is_valid():
            updated_character.save()
            return Response(updated_character.data)
        return Response(updated_character.errors, status=status.HTTP_400_BAD_REQUEST)