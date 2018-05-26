from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from logowanie.models import Student, Admin, Course
from szkolaZarzadzanie.settings import adminKey
from django.template import Context

def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]


def adminCourses(request):
    try:
        temp = request.session["admin"]
    except KeyError:
        return HttpResponseRedirect("panel")
    if request.session["admin"]==adminKey:
        loggedAdmin = Admin.objects.get(email=request.session["email"])
        adminsCourses = list(Course.objects.filter(students=loggedAdmin.id))
        context=[]
        for i in adminsCourses:
            context.append(i.returnCoursName())
        return render(request, 'adminPanelCourses.html', {'courses':context, "student":loggedAdmin})
    else:
        HttpResponseRedirect("panel")


def studentCourses(request):
    try:
        temp = request.session["email"]
    except KeyError:
        return HttpResponseRedirect("logowanie")
    loggedStudent = Student.objects.get(email=request.session["email"])
    studentsCourses = list(Course.objects.filter(students=loggedStudent.id))
    context = []
    for i in studentsCourses:
        context.append(i.returnCoursName())
    return render(request, 'studentPanelCourses.html', {'courses': context, 'student' : loggedStudent})