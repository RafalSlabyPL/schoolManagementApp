from django.shortcuts import render, HttpResponse
from .form import RegisterForm
from .models import User
# Create your views here.

def createUser(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            newUserObj = User()
            newUserObj.name = form.cleaned_data['your_name']
            newUserObj.surname = form.cleaned_data['your_surname']
            newUserObj.email = form.cleaned_data['your_email']
            newUserObj.password = form.cleaned_data['your_password']
            newUserObj.save()
            return HttpResponse('dziala')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()

    return render(request, 'registerForm.html', {'form': form})

def registerForm(request):
    #return render(request, 'mainSite.html')
    return render(request, 'registerForm.html', {'form' : RegisterForm})