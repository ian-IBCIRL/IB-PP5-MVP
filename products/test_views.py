from django.test import TestCase
from .models import Product


class TestModels(TestCase):
    """
    Test for models
    """

    fixtures = [
        'categories.json',
        'user.json',
        'May23datadump.json',
        'checkout.json'
    ]

    def test_product_page(self):
        """
        Test product page
        """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
