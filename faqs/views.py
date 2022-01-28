from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Faqs
from .forms import FaqForm


# Create your views here.
def faqs(request):
    """ A view to render the faqs page """

    faq = Faqs.objects.all()

    context = {

        'faqs': faq,

    }

    return render(request, 'faqs/faqs.html', context=context)


@login_required
def add_faq(request):
    """ Add a faq to the faqs """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin users can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = FaqForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added an faq!')
            return redirect(reverse('faqs'))
        else:
            messages.error(request, 'Failed to add faq. Please ensure the form is valid.')
    else:
        form = FaqForm()
        
    template = 'faqs/add_faq.html'
    context = {
        'form': form,
    }

    return render(request, template, context)



@login_required
def edit_faq(request, faq_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only only admin users can do that.')
        return redirect(reverse('home'))

    faq = get_object_or_404(Faqs, pk=faq_id)
    if request.method == 'POST':
        form = FaqForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated!')
            return redirect(reverse('faqs'))
        else:
            messages.error(request, 'Failed to update. Please ensure the form is valid.')
    else:
        form = FaqForm(instance=faq)

    template = 'faqs/edit_faq.html'
    context = {
        'form': form,
        'faq': faq,
    }

    return render(request, template, context)