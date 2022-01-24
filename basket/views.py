from django.shortcuts import render, redirect
from products.models import Category

# Create your views here.

def view_basket(request):
    """ A view to render the basket and items """
    
    categories = Category.objects.all

    context = {
        'categories': categories,
    }

    return render(request, 'basket/basket.html', context)


def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(redirect_url)