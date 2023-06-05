from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from profiles.models import UserProfile
from checkout.models import Order


class TestCheckoutViews(TestCase):

    fixtures = [
        'categories.json',
        'user.json',
        'May23datadump.json',
        'checkout.json'
    ]

    def test_Checkout_get(self):
        resp = self.client.get(reverse('checkout'))
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, "/products/")

    def test_Checkout_out_success_view(self):
        user = User.objects.get(id=1)
        order_num = Order.objects.get(id=1)
        print("Checkout success order number is ", order_num)

        order = order_num.order_number
        print("Checkout success order is ", order)

        resp = self.client.get(
            f'/checkout/checkout_success/{order}')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'checkout/checkout_success.html')

    def test_abstract_user_Checkout_out_success_view(self):
        order_num = Order.objects.get(id=5)
        print("abstract order number is ", order_num)

        order = order_num.order_number
        print("abstract order is ", order)

        resp = self.client.get(
            f'/checkout/checkout_success/{order}')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'checkout/checkout_success.html')

    def test_cache_checkout_data_get(self):
        resp = self.client.get('/checkout/cache_checkout_data/')
        self.assertEqual(resp.status_code, 405)
