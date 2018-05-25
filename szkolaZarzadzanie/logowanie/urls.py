from django.contrib import admin
from django.urls import path, include
from . import  views

urlpatterns = [
    path('', views.studentPanel, name="rejestruj"),
    path('rejestruj', views.register, name="rejestruj"),
    path('panel', views.studentPanel, name="panel"),
    path('logowanie', views.logIn, name="login"),
    path('wylogowywanie', views.logOut, name="logout"),
    path('oceny', views.oceny, name="oceny"),
    path('wylogowywanie', views.logOut, name="rejestruj"),
    path('wylogowywanie', views.logOut, name="rejestruj"),
]