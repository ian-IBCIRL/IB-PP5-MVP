from django.test import TestCase
from .models import Faqs


class TestModels(TestCase):
    """
    Test for FAQ model
    """

    def test_if_it_returns_a_question(self):
        """
        Test to see if it returns a string
        """
        faq = Faqs.objects.create(
            category='OR',
            questions='Test Question',
            answers='Test Answer'
        )
        self.assertEqual(str(faq), 'Test Question')
