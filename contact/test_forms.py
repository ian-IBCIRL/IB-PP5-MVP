from django.test import TestCase
from .forms import ContactForm


class TestForm(TestCase):
    """
    Test the form
    """

    def test_contact_form(self):
        """
        Test if all the fields are displayed in the form
        """
        form = ContactForm()
        self.assertEqual(form.Meta.fields, '__all__')

    def test_item_is_required_contact_form(self):
        """
        Check if following fields field are required
        """
        form = ContactForm({
            'topic': '',
            'name': '',
            'email': '',
            'phone': '',
            'message': '',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('topic', form.errors.keys())
        self.assertIn('name', form.errors.keys())
        self.assertIn('email', form.errors.keys())
        self.assertIn('phone', form.errors.keys())
        self.assertIn('message', form.errors.keys())
        self.assertEqual(
            form.errors['topic'][0], 'This field is required.')
        self.assertEqual(
            form.errors['name'][0], 'This field is required.')
        self.assertEqual(
            form.errors['email'][0], 'This field is required.')
        self.assertEqual(
            form.errors['phone'][0], 'This field is required.')
        self.assertEqual(
            form.errors['message'][0], 'This field is required.')