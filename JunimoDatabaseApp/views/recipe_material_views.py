from rest_framework.response import Response
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.middleware.csrf import get_token

from JunimoDatabaseApp.models import resource
from ..models.blueprint import Blueprint
from ..models.resource import Resource
from ..serializers import RecipeMaterialSerializer

# Create your views here.
class RecipeMaterials(generics.ListCreateAPIView):
    serializer_class = RecipeMaterialSerializer
    def get(self, request):
        """Index request"""
        # Get all the resources:
        recipe_materials = RecipeMaterials.objects.all()
        # Run the data through the serializer
        data = RecipeMaterialSerializer(recipe_materials, many=True).data
        return Response({ 'recipe_materials': data })


class RecipeMaterialDetail(generics.RetrieveUpdateDestroyAPIView):
    def get(self, request, pk):
        """Show request"""
        # Locate the resource to show
        recipe_material = get_object_or_404(RecipeMaterials, pk=pk)

        # Run the data through the serializer so it's formatted
        data = RecipeMaterialSerializer(recipe_material).data
        return Response({ 'recipe_material': data })