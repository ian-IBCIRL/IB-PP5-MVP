from django.test import TestCase
from .forms import FaqsForm


class TestForm(TestCase):
    """
    Test for the form
    """

    def test_all_item_is_required(self):
        """
        Check if all the field is required
        """
        form = FaqsForm({
            'category': '',
            'questions': '',
            'answers': ''
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['category'][0], 'This field is required.')
        self.assertEqual(form.errors['questions']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['answers'][0], 'This field is required.')

    def test_all_fields_are_displayed_in_the_form(self):
        form = FaqsForm()
        self.assertEqual(form.Meta.fields, '__all__')
