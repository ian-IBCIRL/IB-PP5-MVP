from django.test import TestCase
from django.shortcuts import HttpResponse,  get_object_or_404
from .models import Product, Category, Comment
from .forms import ProductForm, CommentForm


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

    def test_all_item_is_required(self):
        """
        Check if all the field are required
        """
        form = ProductForm({
            'name': '',
            'sku': '',
            'slug': '',
            'price': '',
            'discount_price': '',
            'rating': '',
            'image': '',
            'featured': ''
        })

        self.assertFalse(form.is_valid())

        self.assertEqual(form.errors['name']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['description']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['slug']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['price']
                         [0], 'This field is required.')

    def test_all_fields_are_displayed_in_the_form(self):
        form = ProductForm()
        print("form fields are: ", form.Meta.fields)
        self.assertEqual(form.Meta.fields,
                         (
                            '__all__'
                         ))

    def test_all_fields_are_displayed_in_the_commentform(self):
        form = CommentForm()
        print("form fields are: ", form.Meta.fields)
        self.assertEqual(form.Meta.fields,
                         (
                            'name',
                            'body',
                         ))
