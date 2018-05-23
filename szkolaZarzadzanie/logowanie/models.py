from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20, blank=False)
    surname = models.CharField(max_length=20, blank=False)
    email = models.CharField(max_length=20, blank=False)
    password = models.CharField(max_length=30, blank=False)
    phoneNumber = models.CharField(max_length=30, blank=False)
    city = models.CharField(max_length=30, blank=True)
    region = models.CharField(max_length=30, blank=True)
    postalCode = models.CharField(max_length=10, blank=False)
    street = models.CharField(max_length=100, blank= False)
    homeNumber = models.IntegerField(blank=False)
    apartmentNumber = models.IntegerField(blank=True)
    PESEL = models.IntegerField(blank=False)

    def __str__(self):
        return str(self.email)
