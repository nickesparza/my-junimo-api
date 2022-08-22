#library/urls.py
from django.urls import path
from .views import CharactersView

urlpatterns = [
    path('', CharactersView.as_view(), name='characters'),
    # path('<int:character_id>', character_show, name="character_show")
]