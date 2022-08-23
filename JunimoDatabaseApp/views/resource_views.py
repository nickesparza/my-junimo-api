from rest_framework.response import Response
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.middleware.csrf import get_token

from JunimoDatabaseApp.models import resource
from ..models.resource import Resource
from ..serializers import ResourceSerializer

# Create your views here.
class Resources(generics.ListCreateAPIView):
    serializer_class = ResourceSerializer
    authentication_classes = ()
    permission_classes = ()
    def get(self, request):
        """Index request"""
        # Get all the resources:
        resources = Resource.objects.all()
        # Run the data through the serializer
        data = ResourceSerializer(resources, many=True).data
        return Response({ 'resources': data })


class ResourceDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = ()
    permission_classes = ()
    def get(self, request, pk):
        """Show request"""
        # Locate the resource to show
        resource = get_object_or_404(Resource, pk=pk)

        # Run the data through the serializer so it's formatted
        data = ResourceSerializer(resource).data
        return Response({ 'resource': data })