from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Gallery
from .forms import ImageForm

# Create your views here.
def gallery(request):
    """ A view to render the gallery page """

    images = Gallery.objects.all()

    context = {

        'images': images,

    }

    return render(request, 'gallery/gallery.html', context)


# @login_required
def add_image(request):
    """ Add a image to the gallery """
    # if not request.user.is_superuser:
    #     messages.error(request, 'Sorry, only admin users can do that.')
    #     return redirect(reverse('home'))

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added an Image!')
            return redirect(reverse('gallery'))
        else:
            messages.error(request, 'Failed to add image. Please ensure the form is valid.')
    else:
        form = ImageForm()
        
    template = 'gallery/add_image.html'
    context = {
        'form': form,
    }

    return render(request, template, context)