from django import forms
from . import functions

class RegisterForm(forms.Form):
    your_name = forms.CharField(
        label='Imię',
        max_length=20,
        required=True,
        help_text="",
        widget=forms.TextInput(attrs={'class': "form-control"}))

    your_surname = forms.CharField(
        label='Nazwisko',
        max_length=20,
        required=True,
        widget = forms.TextInput(attrs={'class': "form-control"}))

    your_email = forms.EmailField(
        label='Adres email',
        max_length=50,
        required=True,
        help_text="Nie udostępniamy emaili osobom 3. Są one używane wyłącznie na potrzeby kontaktu ze studentem oraz\
        wysyłania istotnich informacji.",
        widget=forms.TextInput(attrs={'class': "form-control"})
       )

    your_password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password:', 'class': 'form-control'}),
        label='Hasło',
        max_length=30,
    )

    your_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password:', 'class': 'form-control'}),
        label='Powtórz hasło',
        max_length=30,
        required=True)

    your_phoneNumber = forms.CharField(
        label='Numer telefonu',
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': "form-control"})
    )

    your_region = forms.CharField(
        label='Województwo',
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': "form-control"})
    )

    your_city = forms.CharField(
        label='Miasto',
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': "form-control"})
    )

    your_postalCode = forms.CharField(
        label='Kod pocztowy',
        max_length=10,
        required=True,
        widget=forms.TextInput(attrs={'class': "form-control"})
    )

    your_street = forms.CharField(
        label='Ulica',
        max_length=100,
        required= True,
        widget=forms.TextInput(attrs={'class': "form-control"})
    )

    your_homeNumber = forms.IntegerField(
        label='Numer domu',
        required=True,
        widget=forms.TextInput(attrs={'class': "form-control"})
    )

    your_apartmentNumber = forms.IntegerField(
        label='Numer mieszkania',
        required=False,
        widget=forms.TextInput(attrs={'class': "form-control"})
    )

    your_PESEL = forms.IntegerField(
        label='Pesel',
        required=False,
        widget=forms.TextInput(attrs={'class': "form-control"})
    )

    def clean_your_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("your_password1")
        password2 = self.cleaned_data.get("your_password2")
        email = self.cleaned_data.get("email")
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError("Passwords don't match")
        return password2

    def clean_your_email(self):
        email = self.cleaned_data["email"]
        if email and Student.objects.filter(email=email):
            raise forms.ValidationError("This email has already been registered")
        return email


class LogInForm(forms.Form):
    your_email = forms.EmailField(
        label='Adres email',
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'class': "form-control"})
    )

    your_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password:', 'class': 'form-control'}),
        label='Hasło',
        max_length=30
    )
