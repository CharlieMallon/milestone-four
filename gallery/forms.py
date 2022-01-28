from django import forms
from .models import Gallery


class ImageForm(forms.ModelForm):

    class Meta:
        model = Gallery
        fields = '__all__'