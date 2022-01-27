from django.shortcuts import render

from .models import faqs

# Create your views here.
def faqs(request):
    """ A view to render the index page """
    

    faq = faqs.objects.all()

    context = {

        'faqs': faq,

    }

    return render(request, 'faqs/faqs.html', context=context)