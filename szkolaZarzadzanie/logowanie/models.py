from django.db import models


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
    #registrationDate = models.DateTimeField(blank=True) # uzupelnic
    #miastoZajec = models.CharField(max_length=20, blank=False)
    nameAndSurname = str(name) + " " + str(surname)

    def __str__(self):
        return str(self.name) + " " + str(self.surname)


class Admin(Student):
    adminStatus = models.BooleanField(blank=False)


class Homework(models.Model):
    id = models.AutoField(primary_key=True)
    contents = models.CharField(max_length=3000, blank=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=False)
    grade = models.CharField(max_length=10, blank=True)
    comment = models.CharField(max_length=1000, blank=True)
    solution = models.FileField(blank=True)
    #dateAssignment = models.DateTimeField(blank=True)
    #dateUpload = models.DateTimeField(blank=True) # uzupel;nic


class PaymentHistory(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=False)

class SinglePayment(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(blank=True) # uzupelnic
    price = models.IntegerField()
    paymentID = models.CharField(max_length=50)
    paymentHistory = models.ForeignKey(PaymentHistory, on_delete=models.CASCADE, blank=False)

class StudentsGrades(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=False)

class SingleGrade(models.Model):
    id = models.AutoField(primary_key=True)
    grade = models.CharField(max_length=50, blank=False)
    StudentsGrades =  models.ForeignKey(StudentsGrades, on_delete=models.CASCADE, blank=False)


class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    teacher = models.CharField(max_length=150)












