from django.contrib import admin
from . models import Student,Admin, Homework, PaymentHistory, SinglePayment, StudentsGrades, SingleGrade, Course
# Register your models here.
admin.site.register(Student)
admin.site.register(Admin)
admin.site.register(Homework)
admin.site.register(PaymentHistory)
admin.site.register(SingleGrade)
admin.site.register(SinglePayment)
admin.site.register(StudentsGrades)
admin.site.register(Course)