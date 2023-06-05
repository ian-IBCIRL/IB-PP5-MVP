from django.test import TestCase
from .models import Contact, Address


class TestModels(TestCase):
    """
    Test for models
    """

    def test_if_contact_model_returns_a_string(self):
        """
        Test to see if it returns a string
        """
        contact = Contact.objects.create(
            topic='OR',
            name='best client',
            email='bestclient@mail.com',
            phone='16175551212',
            message='Message from best client'
        )
        self.assertEqual(str(contact), 'Message from best client')

    def test_if_address_model_returns_a_string(self):
        """
        Test to see if it returns a string
        """
        address = Address.objects.create(
            address='Main Street Test',
            phone='16175551212',
            email='bestclient@test.com',
        )
        self.assertEqual(str(address), 'Main Street Test')
