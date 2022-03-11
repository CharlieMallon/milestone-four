# pylint: disable=missing-module-docstring
from .models import Gallery

def gallery(request):
    """
    Makes gallery available accross site
    """
    gallery = Gallery.objects.all

    context = {
        'images': gallery,
    }

    return context
