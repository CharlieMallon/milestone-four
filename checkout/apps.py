# pylint: disable=missing-module-docstring
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """ Config Checkout App"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    # This is from the boutique_ado project
    def ready(self):
        import checkout.signals
