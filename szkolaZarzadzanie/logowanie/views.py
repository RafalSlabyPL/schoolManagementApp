from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .form import RegisterForm, LogInForm
from .models import Student

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
    else:
        return render(request, 'registerForm.html', {'form': RegisterForm})

def logIn(request):
    try:
        a = request.session["email"]
    except KeyError:
        if request.method == 'POST':
            form = LogInForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['your_email']
                password = form.cleaned_data['your_password']
                if Student.objects.filter(email=email, password=password).exists():
                    request.session['email'] = email
                    return HttpResponseRedirect("panel")
                else:
                    return render(request, "logInForm.html", {'form': LogInForm, 'error' : 'Podany email i hasło nie pasują do żadnego użytkownika'})
            else:
                return render(request, "logInForm.html", {'form': LogInForm, 'error' : 'Podany mail nie jest poprawny'})

        else:
            return render(request, "logInForm.html", {'form' : LogInForm})
    return HttpResponseRedirect("panel")

def logOut(request):
    try:
        del request.session["email"]
    except KeyError:
        return HttpResponseRedirect("logowanie")
    return HttpResponseRedirect("logowanie")

def studentPanel(request):
    try:
        temp = request.session["email"]
    except KeyError:
        return HttpResponseRedirect("logowanie")
    loggedStudent = Student.objects.get(email=request.session["email"])

    return render(request, 'studentPanel.html', {'student' : loggedStudent})

def oceny(request):
    try:
        temp = request.session["email"]
    except KeyError:
        return HttpResponseRedirect("logowanie")
    loggedStudent = Student.objects.get(email=request.session["email"])
    return render(request, 'studentPanelOceny.html', {'student' : loggedStudent})


