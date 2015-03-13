from django import forms

__author__ = 'Mathieu'


class ConnexionForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class UserCreationForm(forms.Form):
    username = forms.CharField(label="Username", max_length=32)
    first_name = forms.CharField(label="First name", max_length=32)
    last_name = forms.CharField(label="Last name", max_length=32)
    email = forms.EmailField(label="Email", max_length=32)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)