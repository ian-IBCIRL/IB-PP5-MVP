from django.test import TestCase
from .forms import UserProfileForm


class TestForm(TestCase):
    """
    Test the forms
    """

    def test_no_fields_are_required(self):
        """
        Test that none of the form fields are required.
        """
        form = UserProfileForm({})
        self.assertTrue(form.is_valid())
