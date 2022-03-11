# pylint: disable=missing-module-docstring
from django.apps import AppConfig


class ProductsConfig(AppConfig):
    """
    Configure Products App
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
