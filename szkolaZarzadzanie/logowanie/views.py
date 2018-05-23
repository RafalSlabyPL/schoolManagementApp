from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .form import RegisterForm, LogInForm
from .models import Student
# Create your views here.

def register(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            newUserObj = Student()
            newUserObj.name = form.cleaned_data['your_name']
            newUserObj.surname = form.cleaned_data['your_surname']
            newUserObj.email =form.cleaned_data['your_email']
            newUserObj.password = form.cleaned_data['your_password1']
            newUserObj.phoneNumber = form.cleaned_data['your_phoneNumber']
            newUserObj.city = form.cleaned_data['your_city']
            newUserObj.region = form.cleaned_data['your_region']
            newUserObj.postalCode = form.cleaned_data['your_postalCode']
            newUserObj.street = form.cleaned_data['your_street']
            newUserObj.homeNumber = form.cleaned_data['your_homeNumber']
            newUserObj.apartmentNumber = form.cleaned_data['your_apartmentNumber']
            newUserObj.PESEL = form.cleaned_data['your_PESEL']
            newUserObj.save()
            return HttpResponseRedirect('dziala')
        else:
            return HttpResponse(form.errors)


def registerForm(request):
    #return render(request, 'htmlHeadFrame.html')
    return render(request, 'registerForm.html', {'form' : RegisterForm})

def dziala(request):
    return HttpResponse("<h1>Zadzialalo</h1>")

def studentPanel(request):
    return render(request, 'studentPanel.html')

def logIn(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['your_email']
            password = form.cleaned_data['your_password']
            if Student.objects.filter(email=email, password=password).exists():
                return HttpResponseRedirect("panel")
            else:
                return render(request, "logInForm.html", {'form': LogInForm, 'error' : 'Podany email i hasło nie pasują do żadnego użytkownika'})
        else:
            return render(request, "logInForm.html", {'form': LogInForm, 'error' : 'Podany mail nie jest poprawny'})

    else:
        return render(request, "logInForm.html", {'form' : LogInForm})