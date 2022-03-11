# pylint: disable=missing-module-docstring
from django.apps import AppConfig


class FaqsConfig(AppConfig):
    """ Config Faqs App"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'faqs'
