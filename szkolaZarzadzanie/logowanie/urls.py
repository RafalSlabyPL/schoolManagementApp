from django.contrib import admin
from django.urls import path, include
from . import  views

urlpatterns = [
    path('rejestracja', views.registerForm, name="registerForm"),
    path('dziala', views.dziala, name="dziala"),
    path('rejestruj', views.register, name="rejestruj"),
    path('panel', views.studentPanel, name="rejestruj"),
    path('logowanie', views.logIn, name="rejestruj"),

]