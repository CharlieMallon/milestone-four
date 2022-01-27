from django.shortcuts import render

from .models import Gallery

# Create your views here.
def gallery(request):
    """ A view to render the gallery page """

    images = Gallery.objects.all()

    context = {

        'images': images,

    }

    return render(request, 'gallery/gallery.html', context)