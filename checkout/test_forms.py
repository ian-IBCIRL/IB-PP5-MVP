from django.test import TestCase
from .forms import OrderForm


class TestForm(TestCase):
    """
    Test for the form
    """

    def test_all_item_is_required(self):
        """
        Check if all the field are required
        """
        form = OrderForm({
            'full_name': '',
            'email': '',
            'phone_number': '',
            'street_address1': '',
            'street_address2': '',
            'town_or_city': '',
            'county': '',
            'postcode': '',
            'country': ''
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['full_name']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['email']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['phone_number']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['street_address1']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['town_or_city']
                         [0], 'This field is required.')

    def test_all_fields_are_displayed_in_the_form(self):
        form = OrderForm()
        print("form fields are: ", form.Meta.fields)
        self.assertEqual(form.Meta.fields,
                         (
                            'full_name',
                            'email',
                            'phone_number',
                            'street_address1',
                            'street_address2',
                            'town_or_city',
                            'postcode',
                            'country',
                            'county',
                         ))
#        '__all__')
