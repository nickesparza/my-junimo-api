from rest_framework.response import Response

from rest_framework import generics, status
from django.db import models
from django.shortcuts import get_object_or_404
from django.middleware.csrf import get_token

from JunimoDatabaseApp.models import resource
from ..models.blueprint import Blueprint
from ..models.resource import Resource
from ..serializers import RecipeMaterialSerializer
from .blueprint_views import BlueprintDetail

# Create your views here.

# this will return all recipe materials that match one blueprint
class RecipeMaterials(generics.ListCreateAPIView):
    serializer_class = RecipeMaterialSerializer(many=True)
    authentication_classes = ()
    permission_classes = ()
    objects = models.Manager()
    def get(self, request):
        """Index request"""
        # define
        # Get all the resources from recipe materials list
        recipe_materials = Resource.objects.all()
        # Run the data through the serializer
        data = RecipeMaterialSerializer(recipe_materials, many=True).data
        return Response({ 'recipe_materials': data })

# this will return all recipe materials that match one blueprint
class RecipeMaterialDetail(generics.RetrieveUpdateDestroyAPIView):
    # this would limit to logged in users?
    authentication_classes = ()
    # this would limit to owned resources?
    permission_classes = ()
#     # will need to bring over the fk for the blueprint to return materials for
    def get(self, request, fk):
        
        """Show request"""
        # Locate the resource to show
        # blueprint = get_object_or_404(BlueprintDetail, pk=fk)
        recipe_materials = RecipeMaterials.objects.filter(resource_id=fk)
        # Run the data through the serializer so it's formatted
        data = RecipeMaterialSerializer(recipe_materials, many=True).data
        return Response({ 'recipe_materials': data })