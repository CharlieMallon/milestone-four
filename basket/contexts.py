from decimal import Decimal
from django.conf import settings

def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0
    min_order = settings.MINIMUM_ORDER

    if product_count >= min_order:
        checkout = True
    else:
        checkout = False

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = settings.DELIVERY_COST
    else:
        delivery = 0

    grand_total = total + delivery

    context = {
        'basket_items': basket_items ,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
        'checkout': checkout,
    }

    return context