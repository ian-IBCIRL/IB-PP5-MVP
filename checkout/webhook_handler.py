from django.http import HttpResponse

from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

import json
import time
import stripe


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""

        print("trying to send email to", order.email)
        cust_email = order.email
        subject = "Hello World"
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
             {'order': order})
        print("got subject", subject)
        body = "This is the message body"
#        body = render_to_string(
#            'checkout/confirmation_emails/confirmation_email_body.txt',
#            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})
        print("got body", body)
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

        print(subject,
              body,
              settings.DEFAULT_FROM_EMAIL,
              [cust_email])

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        print("handling succeeded")

        intent = event.data.object
        pid = intent.id
        ordersheet = intent.metadata.ordersheet
        save_info = intent.metadata.save_info

        print("got metadata - ordersheet is:", ordersheet)
        print("intent.latest_charge is:", intent.latest_charge)

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )
        print("Got stripe charge")
        # After a Stripe update on November 16, 2022,
        # the charges attribute is no longer available
        # directly from the payment intent. To get the
        # billing_details you will need to use stripe_charge.billing_details
        # and not intent.charges.data[0].billing_details
        # same for .amount

        billing_details = stripe_charge.billing_details  # noqa updated
        print("Got details 1")
        shipping_details = intent.shipping
        print("Got details 2")
        grand_total = round(stripe_charge.amount / 100, 2)  # updated

        print("Got details")

        # clean data in shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = shipping_details.phone
                profile.default_country = shipping_details.address.country
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_town_or_city = shipping_details.address.city
                profile.default_street_address1 = \
                    shipping_details.address.line1
                profile.default_street_address2 = \
                    shipping_details.address.line2
                profile.default_county = shipping_details.address.state
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:

                print("Trying to verify")
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_ordersheet=ordersheet,
                    stripe_pid=pid,
                )
                print("Order is::", order)
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                print("Order Does Not Exist")
                time.sleep(1)

        if order_exists:
            print("Order exists - sending email", order)
            self._send_confirmation_email(order)
            print("Email sent")
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',  # noqa
                status=200)
        else:
            order = None
            try:
                print("trying to create")
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_ordersheet=ordersheet,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(ordersheet).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
            except Exception as e:
                if order:
                    print("deleting order")
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(order)
        print("Sent Email")
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',  # noqa
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
