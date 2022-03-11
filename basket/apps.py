# pylint: disable=missing-module-docstring
from django.apps import AppConfig


class BasketConfig(AppConfig):
    """ Config Basket App"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'basket'
