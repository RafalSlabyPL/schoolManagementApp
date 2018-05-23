from django.contrib import admin
from django.urls import path, include
from . import  views

urlpatterns = [
    path('', views.registerForm, name="registerForm"),
    path('dziala', views.dziala, name="dziala"),
    path('rejestruj', views.register, name="rejestruj"),

]