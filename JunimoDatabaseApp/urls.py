from django.urls import path

from JunimoDatabaseApp.views.blueprint_views import Blueprints, BlueprintDetail
from .views.character_views import Characters, CharacterDetail
from .views.resource_views import Resources, ResourceDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
    # Restful routing
    path('characters/', Characters.as_view(), name='characters'),
    path('characters/<int:pk>/', CharacterDetail.as_view(), name='character_detail'),
    path('blueprints/', Blueprints.as_view(), name='blueprints'),
    path('blueprints/<int:pk>/', BlueprintDetail.as_view(), name='blueprint_detail'),
    path('resources/', Resources.as_view(), name='resources'),
    path('resources/<int:pk>/', ResourceDetail.as_view(), name='resource_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
