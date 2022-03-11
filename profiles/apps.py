# pylint: disable=missing-module-docstring
from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    Configure Profiles App
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
