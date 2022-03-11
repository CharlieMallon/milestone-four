# pylint: disable=missing-module-docstring
from django.apps import AppConfig


class GalleryConfig(AppConfig):
    """
    Configure Gallery App
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gallery'
