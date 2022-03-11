# pylint: disable=missing-module-docstring
from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """
    List out the items in Product Admin
    """
    list_display = (
        "sku",
		"name",
		"description",
		"price",
		"category",
		"image",
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    """
    List out the items in category Admin
    """
    list_display = (
        "name",
        "friendly_name",
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
