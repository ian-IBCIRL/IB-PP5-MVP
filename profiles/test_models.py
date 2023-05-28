from django.test import TestCase
from .models import UserProfile
from django.contrib.auth.models import User


class TestModels(TestCase):
    """
    Test for models
    """

    def test_if_the_model_returns_a_string(self):
        user = User.objects.create_user(
            'ibowell',
        )
        test_profile = UserProfile.objects.get(user=user)
        self.assertEqual(str(test_profile), 'ibowell')
