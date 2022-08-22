# first_app/urls.py
from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('characters/', include('junimoDatabase.urls')),
    path('users/', include('junimoDatabase.urls'))
    #path('', views.index, name='index'),
]