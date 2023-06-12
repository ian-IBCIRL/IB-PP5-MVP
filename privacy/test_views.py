from django.test import TestCase


class TestViews(TestCase):
    """
    Test for the Privacy view
    """

    def test_privacy_page(self):
        """
        Test privacy page
        """
        response = self.client.get('/privacy/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'privacy/privacy.html')
