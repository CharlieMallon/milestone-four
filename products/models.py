# pylint: disable=missing-module-docstring
from django.db import models


class Category(models.Model):
    """Category Model"""
    class Meta:
        """Re-name plural for Category"""
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254, null=False, blank=False)
    friendly_name = models.CharField(max_length=254, null=False, blank=False)
    image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """Returns friendly Name"""
        return self.friendly_name


class Product(models.Model):
    """each product requires a name, description and a price, all other fields are optional"""
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    number_of_cakes = models.DecimalField(max_digits=2, decimal_places=0)

    def __str__(self):
        return self.name
