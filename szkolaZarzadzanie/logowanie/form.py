from django import forms

class RegisterForm(forms.Form):
    your_name = forms.CharField(label='Imię', max_length=20, required=False)
    your_surname = forms.CharField(label='Nazwisko', max_length=20, required=False)
    your_email = forms.CharField(label='Adres email', max_length=20, required=False)
    your_password1 = forms.CharField(widget=forms.PasswordInput, label='Hasło', max_length=30, required=False)
    your_password2 = forms.CharField(widget=forms.PasswordInput, label='Powtórz hasło', max_length=30, required=False)
    your_phoneNumber = forms.CharField(label='Numer telefonu', max_length=30, required=False)
    your_city = forms.CharField(label='Miasto', max_length=30, required=True)
    your_region = forms.CharField(label='Województwo', max_length=30, required=True)
    your_postalCode = forms.CharField(label='Kod pocztowy', max_length=10, required=False)
    your_street = forms.CharField(label='Ulica', max_length=100, required= False)
    your_homeNumber = forms.IntegerField(label='Numer domu', required=False)
    your_apartmentNumber = forms.IntegerField(label='Numer mieszkania', required=True)
    your_PESEL = forms.IntegerField(label='Pesel', required=False)

