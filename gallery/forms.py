from django import forms
from gallery.models import Image, Album


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'description', 'original', 'album']
        

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'description']


class ConnexionForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class UserCreationForm(forms.Form):
    username = forms.CharField(label="Username", max_length=32)
    first_name = forms.CharField(label="First name", max_length=32)
    last_name = forms.CharField(label="Last name", max_length=32)
    email = forms.EmailField(label="Email", max_length=32)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
