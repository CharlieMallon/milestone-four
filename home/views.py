from django.shortcuts import render
from products.models import Category

# Create your views here.

def index(request):
    """ A view to render the index page with the categories on it """

    context = {

    }

    
    return render(request, 'home/index.html', context)