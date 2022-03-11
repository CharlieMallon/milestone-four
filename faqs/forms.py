# pylint: disable=missing-module-docstring
from django import forms
from .models import Faqs


class FaqForm(forms.ModelForm):
    """Create faq form"""
    class Meta:
        """faq form is all field from model"""
        model = Faqs
        fields = '__all__'
