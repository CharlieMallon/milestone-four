# pylint: disable=missing-module-docstring
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from products.models import Product


def view_basket(request):
    """
    A view to render the basket and items
    """

    template = 'basket/basket.html'
    context = {

    }

    return render(request, template, context)


def add_to_basket(request, item_id):
    """
    Add a quantity of the specified product to the shopping basket
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity \
                         to {basket[item_id]}')
    else:
        basket[item_id] = quantity
        messages.success(request, f'Added {basket[item_id]} {product.name} \
                         to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """ Adjust the quantity of the specified product in the shopping basket """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))

    # gets the basket variable if it exists, creates it if it doesn't.
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
        messages.success(request, f'Updated {product.name} quantity \
                         to {basket[item_id]}')
    else:
        basket.pop(item_id)
        messages.success(request, f'Removed {product.name} from your basket')

    request.session['basket'] = basket

    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """
    Remove the specified product in the shopping basket
    """
    try:
        product = get_object_or_404(Product, pk=item_id)

        # gets the basket variable if it exists, creates it if it doesn't.
        basket = request.session.get('basket', {})

        basket.pop(item_id)

        messages.success(request, f'Removed {product.name} \
            from your basket')

        request.session['basket'] = basket

        return HttpResponse(status=200)

    except ObjectDoesNotExist as error:
        messages.error(request, f'Error removing item: {error}')
        return HttpResponse(status=404)
