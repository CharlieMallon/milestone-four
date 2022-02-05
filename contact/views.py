from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactForm
from profiles.models import UserProfile


# Create your views here.
def contact(request):
    """
    A view to render the contact page
    """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully contacted us!')
            message = {
                'full_name': request.POST['full_name'],
                'email': request.POST['email'],
                'subject': request.POST['subject'],
                'message_text': request.POST['message_text'],
            }
            print(message)
            # _send_contact_email(message)
            return redirect(reverse('contact'))
        else:
            messages.error(request, 'Failed to contact us. Please ensure the form is valid.')
    else:
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                form = ContactForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                })
            except UserProfile.DoesNotExist:
                form = ContactForm()
        else:
            form = ContactForm()

    template = 'contact/contact.html'
    context = {
    'form': form,
    }

    return render(request, template, context)


def _send_contact_email(message):
        """Send the user a confirmation email"""
        cust_email = message.email
        subject = message.subject
        body = message.message_text
        
        send_mail(
            subject,
            body,
            [cust_email],
            settings.DEFAULT_FROM_EMAIL
        )