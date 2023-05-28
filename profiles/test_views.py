from django.test import TestCase
from django.contrib.auth.models import User


class TestViews(TestCase):
    """
    Test for the views
    """

    def setUp(self):
        self.user = User.objects.create_user(
            'testuser', 'ibowellms@email.com', 'testuser'
        )
        print("\nsetup test user as", self.user)

    def test_profile_page(self):
        """
        Test if the profile page loads
        """
        print("\ntesting if profile page loads")
        self.client.login(username='testuser', password='testuser')
        response = self.client.get('/profiles/')
        print("\nresponse is", response)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
