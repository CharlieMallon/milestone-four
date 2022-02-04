from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from checkout.models import Order

# Create your views here.

def index(request):
    """ A view to render the index page """
    
    return render(request, 'home/index.html')


@login_required
def manage_shop(request):
    """ A view to render the shop manager """
    orders = Order.objects.all()
    template = 'home/manage.html'
    context = {
        'orders': orders,
    }

    return render(request, template, context)