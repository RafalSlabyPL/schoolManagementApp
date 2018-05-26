from django.shortcuts import render, HttpResponseRedirect
from logowanie.models import Student, Admin
from szkolaZarzadzanie.settings import adminKey

def adminGrades(request):
    try:
        temp = request.session["admin"]
    except KeyError:
        return HttpResponseRedirect("panel")
    if request.session["admin"]==adminKey:
        loggedAdmin = Admin.objects.get(email=request.session["email"])
        return render(request, 'adminPanelOceny.html', {'student': loggedAdmin})
    else:
        HttpResponseRedirect("panel")


def studentGrades(request):
    try:
        temp = request.session["email"]
    except KeyError:
        return HttpResponseRedirect("logowanie")
    loggedStudent = Student.objects.get(email=request.session["email"])
    return render(request, 'studentPanelOceny.html', {'student' : loggedStudent})