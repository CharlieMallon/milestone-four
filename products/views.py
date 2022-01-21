from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models import Q

from .models import Product, Category

# Create your views here.
def all_products(request):
    """A view to show all products, including sorting and search categories"""

    products = Product.objects.all()
    categories = Category.objects.all
    query = None
    search_categories = None
    

    if request.GET:

        if 'category' in request.GET:
                search_categories = request.GET['category'].split(',')
                products = products.filter(category__name__in=search_categories)
                search_categories = Category.objects.filter(name__in=search_categories)
    
        if 'q' in request.GET:            
            query = request.GET['q']
            if not query:
                messages.error(request, 'You did not enter a search criteria')
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products=products.filter(queries)
    
    context = {
        'products': products,
        'search_term': query,
        'current_categories': search_categories,
        'categories': categories,
    }

    return render(request, 'products/products.html', context)
