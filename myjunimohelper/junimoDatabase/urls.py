#library/urls.py
from django.urls import path
from .views import character_show, index

urlpatterns = [
    path('', index, name='characters'),
    path('<int:character_id>', character_show, name="character_show")
]