from django.contrib import admin
from django.urls import path, include
from . import  views

urlpatterns = [

    path('rejestruj', views.register, name="rejestruj"),
    path('logowanie', views.logIn, name="login"),
    path('wylogowywanie', views.logOut, name="logout"),
]