from django.shortcuts import render
from products.models import Category

# Create your views here.

def view_basket(request):
    """ A view to render the basket and items """
    
    categories = Category.objects.all

    context = {
        'categories': categories,
    }

    
    return render(request, 'basket/basket.html', context)