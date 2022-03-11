# pylint: disable=missing-module-docstring
from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """ Add/edit Product form """
    class Meta:
        """ Product form """
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names


class CategoryForm(forms.ModelForm):
    """ Add/edit Category form """
    class Meta:
        """ Category form """
        model = Category
        fields = '__all__'
