from django.shortcuts import render
from django.contrib import messages

from django.core.mail import send_mail
from django.conf import settings

from django.template.loader import render_to_string

from .models import Address
from .forms import ContactForm


def contact(request):
    """
    Customers can send a message with the form
    """

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

            # Confirmation email is sent on submission of form
            topic = form.cleaned_data['topic']
            name = form.cleaned_data['name']
            original_message = form.cleaned_data['message']
            message = render_to_string(
                'contact/confirmation_email/confirmation_email.txt', {
                    'name': name,
                    'original_message': original_message
                })
            email_from = settings.DEFAULT_FROM_EMAIL
            email_to = [form.cleaned_data['email']]

            send_mail(
                topic,
                message,
                email_from,
                email_to
            )

            messages.success(request, 'Message submitted and a confirmation \
                email has gone out with a copy of the original message')

    form = ContactForm
    company_address = Address.objects.all()

    context = {
        'form': form,
        'company_address': company_address,
    }

    template = 'contact/contact.html'

    return render(request, template, context)
