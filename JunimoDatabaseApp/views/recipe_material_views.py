from rest_framework.response import Response

from rest_framework import generics, status
from django.db import models
from django.shortcuts import get_object_or_404
from django.middleware.csrf import get_token

from ..models.blueprint import Blueprint
from ..models.recipe_material import RecipeMaterial
from ..serializers import RecipeMaterialSerializer

# Create your views here.

# this will return all recipe materials that match one blueprint
class RecipeMaterialsView(generics.ListCreateAPIView):
    serializer_class = RecipeMaterialSerializer
    authentication_classes = ()
    permission_classes = ()
    def get(self, request, pk):
        """Index request"""
        request = request
        blueprint = get_object_or_404(Blueprint, pk=pk)
        recipe_materials = RecipeMaterial.objects.filter(blueprint_id=blueprint)
        data = RecipeMaterialSerializer(recipe_materials, many=True).data
        return Response({ 'recipe_materials': data })

# this should return ONE recipe material based on pk (recipe material)
class RecipeMaterialDetailView(generics.RetrieveUpdateDestroyAPIView):
    # this would limit to logged in users?
    serializer_class = RecipeMaterialSerializer
    authentication_classes = ()
    permission_classes = ()
    def get(self, request, pk):
        """Show request"""
        recipe_material = get_object_or_404(RecipeMaterial, pk=pk)
        # Run the data through the serializer so it's formatted
        data = RecipeMaterialSerializer(recipe_material).data
        return Response({ 'recipe_materials': data })