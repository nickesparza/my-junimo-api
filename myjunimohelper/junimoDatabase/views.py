from django.shortcuts import render
from django.http import JsonResponse
from models import Character, Resource, Blueprint, Inventory, RecipeMaterials

# Create your views here.
def index(request):
    characters = Character.objects.all()
    data = list(characters.values())
    return JsonResponse(data)