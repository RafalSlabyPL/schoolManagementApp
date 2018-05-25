from django.shortcuts import render, HttpResponseRedirect
from szkolaZarzadzanie.logowanie.models import Admin, Student
from szkolaZarzadzanie.szkolaZarzadzanie.settings import adminKey

def adminPanel(request):
    try:
        temp = request.session["admin"]
    except KeyError:
        return HttpResponseRedirect("panel")
    if request.session["admin"]==adminKey:
        loggedAdmin = Admin.objects.get(email=request.session["email"])
        return render(request, 'adminPanel.html', {'student' : loggedAdmin})
    else:
        HttpResponseRedirect("panel")

def studentPanel(request):
    try:
        temp = request.session["email"]
    except KeyError:
        return HttpResponseRedirect("logowanie")
    loggedStudent = Student.objects.get(email=request.session["email"])
    return render(request, 'studentPanel.html', {'student' : loggedStudent})
