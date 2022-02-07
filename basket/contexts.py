from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0
    cake_count = 0
    min_order = settings.MINIMUM_ORDER
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        cake_count += quantity * product.number_of_cakes
        total += quantity * product.price
        product_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if cake_count >= min_order:
        checkout = True
    else:
        checkout = False

    delta = min_order - cake_count

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = settings.DELIVERY_COST
    else:
        delivery = 0

    grand_total = total + delivery

    print(basket_items)

    context = {
        'basket_items': basket_items,
        'product_count': product_count,
        'delta': delta,
        'delivery': delivery,
        'total': total,
        'grand_total': grand_total,
        'checkout': checkout,
    }

    return context