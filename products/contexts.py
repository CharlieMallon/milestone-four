# pylint: disable=missing-module-docstring
from .models import Category


def categories(request):
    """
    Makes categories available accross site
    """
    categories = Category.objects.all

    context = {
        'categories': categories,
    }

    return context
