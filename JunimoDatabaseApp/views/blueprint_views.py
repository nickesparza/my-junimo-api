from rest_framework.response import Response
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.middleware.csrf import get_token

from ..models.blueprint import Blueprint
from ..serializers import BlueprintSerializer

# Create your views here.
class Blueprints(generics.ListCreateAPIView):
    serializer_class = BlueprintSerializer
    authentication_classes = ()
    permission_classes = ()
    def get(self, request):
        """Index request"""
        # Get all the resources:
        blueprints = Blueprint.objects.all()
        # Run the data through the serializer
        data = BlueprintSerializer(blueprints, many=True).data
        return Response({ 'blueprints': data })


class BlueprintDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = ()
    permission_classes = ()
    def get(self, request, pk):
        """Show request"""
        # Locate the resource to show
        blueprint = get_object_or_404(Blueprint, pk=pk)

        # Run the data through the serializer so it's formatted
        data = BlueprintSerializer(blueprint).data
        return Response({ 'blueprint': data })