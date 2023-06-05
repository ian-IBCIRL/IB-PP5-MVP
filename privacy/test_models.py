from django.test import TestCase
# from django.db import models
from .models import Privacy


class TestModels(TestCase):
    """
    Test for models
    """

    def test_if_the_model_returns_a_string(self):
        """
        Test to see if it returns a string
        """
        privacytest = Privacy.objects.create(
            title='Test Privacy Policy',
            privacy_policy="This is our Privacy Policy"
        )
        self.assertEqual(str(privacytest.title), 'Test Privacy Policy')
        self.assertEqual(str(privacytest.privacy_policy), 'This is our Privacy Policy')
