from django.shortcuts import render
from products.models import Category

# Create your views here.

def index(request):
    """ A view to render the index page with the categories on it """
    
    categories = Category.objects.all

    context = {
        'categories': categories,
    }

    
    return render(request, 'home/index.html', context)