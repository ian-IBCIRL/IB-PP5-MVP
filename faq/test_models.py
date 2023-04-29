from django.test import TestCase
from .models import Faq


class TestModels(TestCase):
    """
    Test for models
    """

    def test_if_it_returns_a_question(self):
        """
        Test to see if it returns a string
        """
        faq = Faq.objects.create(
            category='OR',
            questions='Test Question',
            answers='Test Answer'
        )
        self.assertEqual(str(faq), 'Test Question')
