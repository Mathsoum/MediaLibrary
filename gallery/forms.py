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
