#library/urls.py
from django.urls import path
from .views import CharactersView, SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
    path('', CharactersView.as_view(), name='characters'),
    # path('<int:character_id>', character_show, name="character_show"),
    # path('users/sign-up/', SignUp.as_view(), name='sign-up'),
    # path('users/sign-in/', SignIn.as_view(), name='sign-in'),
    # path('users/sign-out/', SignOut.as_view(), name='sign-out'),
    # path('users/change-pw/', ChangePassword.as_view(), name='change-pw'),
]