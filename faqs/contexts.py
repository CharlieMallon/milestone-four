# pylint: disable=missing-module-docstring
from .models import Faqs


def faqs(request):
    """
    Makes faqs available accross site
    """
    faqs = Faqs.objects.all

    context = {
        'faqs': faqs,
    }

    return context
