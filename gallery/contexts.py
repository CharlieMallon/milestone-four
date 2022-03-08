
from .models import Gallery

def gallery(request):


    gallery = Gallery.objects.all

    context = {
        'images': gallery,
    }

    return context