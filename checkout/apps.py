from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    # This is from the boutique_ado project
    def ready(self):
        import checkout.signals