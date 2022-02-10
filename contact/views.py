from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .forms import ContactForm
from .models import Contact
from profiles.models import UserProfile


# Create your views here.
def contact(request):
    """
    A view to render the contact page
    """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            print(message)
            try:
                _send_contact_email(message)
            except:
                messages.error(request, 'Something went wrong, please try again later')
                message.message_status = 'submitted but not sent'
                message.save()
            else:
                messages.success(request, 'Successfully contacted us!')
                message.message_status = 'submitted and sent'
                message.save()


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
        body = render_to_string(
            'contact/contact_emails/contact_email_body.txt',
            {'message': message})
        
        send_mail(
            subject,
            body,
            cust_email,
            [settings.DEFAULT_FROM_EMAIL]
        )