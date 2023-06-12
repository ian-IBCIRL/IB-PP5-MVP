from django.test import TestCase
from django.shortcuts import HttpResponse,  get_object_or_404
from .models import Product, Category


class TestModels(TestCase):
    """
    Test for Product model
    """

    fixtures = [  # set up test data
        'categories.json',
        'user.json',
        'May23datadump.json',
        'checkout.json'
    ]

    def test_if_the_model_returns_a_string(self):

        product = Product.objects.get(pk=1)

        self.assertEqual(str(product.name), 'Information Security Policy')
        self.assertEqual(str(product.sku), 'pp5001340155a')

        product = Product.objects.get(pk=2)

        self.assertEqual(str(product.name), 'Data Protection Policy')
        self.assertEqual(str(product.sku), 'pp5001600425a')
