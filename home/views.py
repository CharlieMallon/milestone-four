# pylint: disable=missing-module-docstring
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from checkout.models import Order


def index(request):
    """
    A view to render the index page
    """
    template = 'home/index.html'
    return render(request, template)


@login_required
def manage_shop(request):
    """
    A view to render the shop manager page
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin users can do that.')
        return redirect(reverse('home'))

    orders = Order.objects.all()
    template = 'home/manage.html'
    context = {
        'orders': orders,
    }

    return render(request, template, context)
