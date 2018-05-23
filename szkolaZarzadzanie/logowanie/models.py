from django.db import models

# Create your models here.

class Student(models.Model):
    id = models.AutoField(primary_key=True)
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
        return str(self.name) + " " + str(self.surname)

class Homework(models.Model):
    contents = models.CharField(max_length=3000, blank=False)
    #varriable student containt foreign key of sutent profile
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=False)
    grade = models.CharField(max_length=10, blank=True)
    comment = models.CharField(max_length=1000, blank=True)
    grade = models.FileField(blank=True)









