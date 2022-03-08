
from .models import Faqs

def faqs(request):


    faqs = Faqs.objects.all

    context = {
        'faqs': faqs,
    }

    return context