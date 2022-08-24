from rest_framework.response import Response
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.middleware.csrf import get_token

from JunimoDatabaseApp.models import material
from ..models.material import Material
from ..serializers import MaterialSerializer

# Create your views here.
class Materials(generics.ListCreateAPIView):
    serializer_class = MaterialSerializer
    authentication_classes = ()
    permission_classes = ()
    def get(self, request):
        """Index request"""
        # Get all the resources:
        materials = Material.objects.all()
        # Run the data through the serializer
        data = MaterialSerializer(materials, many=True).data
        return Response({ 'materials': data })


class MaterialDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MaterialSerializer
    authentication_classes = ()
    permission_classes = ()
    def get(self, request, pk):
        """Show request"""
        # Locate the material to show
        material = get_object_or_404(Material, pk=pk)

        # Run the data through the serializer so it's formatted
        data = MaterialSerializer(material).data
        return Response({ 'material': data })