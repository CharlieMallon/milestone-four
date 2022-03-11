# pylint: disable=missing-module-docstring
from django import forms
from .models import Gallery


class ImageForm(forms.ModelForm):
    """ Form to add/edit image in gallery """
    class Meta:
        """ Import Fields """
        model = Gallery
        fields = '__all__'
