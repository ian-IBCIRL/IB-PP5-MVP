from django.test import TestCase
from django.contrib.auth.models import User
from .models import Faq


class TestViews(TestCase):
    """
    Test for the views
    """
    # ----------------- Test all the urls

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'admin', 'admin@email.com', 'adminpassword'
        )

        self.user = User.objects.create_user(
            'ib', 'ib@email.com', 'ibpassword'
        )

        self.faq = Faq.objects.create(
            category='OR',
            questions='sample question',
            answers='sample answers'
        )

    def test_faq_page(self):
        """
        Test faq page
        """
        response = self.client.get('/faq/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'faq/faq.html')

    def test_add_faq_page(self):
        """
        Test if the add_faq page loads
        """
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get('/faq/add_faq/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'faq/add_faq.html')

    def test_edit_faq_page(self):
        """
        Test if the edit page loads
        """
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(f'/faq/edit_faq/{self.faq.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'faq/edit_faq.html')

    def test_delete_faq_page(self):
        """
        Test to check if delete page redirects
        """
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(f'/faq/delete_faq/{self.faq.id}/')
        self.assertEqual(response.status_code, 302)

    # ----------------- End of url test

    def test_add_faq(self):
        """
        Test if the view creates a new faq
        """
        self.client.login(username='admin', password='adminpassword')
        # check if the form is valid
        response = self.client.post(
            '/faq/add_faq/', {
                'category': 'OT',
                'questions': 'Sample Question',
                'answers': 'Sample Answers'
            }, follow=True  # the client will follow the redirect
        )
        self.assertEqual(response.status_code, 200)

        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "success")
        self.assertTrue("FAQ added successfully!" in message.message)

    def test_edit_faq(self):
        """
        Test if the edit view lets you edit the faq
        """
        self.client.login(username='admin', password='adminpassword')
        # check if the form is valid
        response = self.client.post(
            f'/faq/edit_faq/{self.faq.id}/', {
                'category': 'OT',
                'questions': 'Sample Question',
                'answers': 'Sample Answers'
            }, follow=True  # the client will follow the redirect
        )
        self.assertEqual(response.status_code, 200)

        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "success")
        self.assertTrue("FAQ updated successfully!" in message.message)

    def test_delete_faqs(self):
        """
        Test if the edit view lets you edit the faq
        """
        self.client.login(username='admin', password='adminpassword')
        response = self.client.post(
            f'/faq/delete_faq/{self.faq.id}/'
        )
        self.assertEqual(response.status_code, 302)

    # Superuser functionality
    def test_only_superuser_can_add(self):
        """
        Test if the edit view lets you edit the faq
        """
        self.client.login(username='ib', password='ibpassword')
        response = self.client.post(
            f'/faq/add_faq/', follow=True
        )
        self.assertEqual(response.status_code, 200)

        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "error")
        self.assertTrue(
            'Sorry - You are not authorised' in message.message)

    def test_only_superuser_can_edit(self):
        """
        Test if the edit view lets you edit the faq
        """
        self.client.login(username='ib', password='ibpassword')
        response = self.client.post(
            f'/faq/edit_faq/{self.faq.id}/', follow=True
        )
        self.assertEqual(response.status_code, 200)

        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "error")
        self.assertTrue(
            'Sorry - You are not authorised' in message.message)

    def test_only_superuser_can_delete(self):
        """
        Test if the edit view lets you edit the faq
        """
        self.client.login(username='ib', password='ibpassword')
        response = self.client.post(
            f'/faq/delete_faq/{self.faq.id}/', follow=True
        )
        self.assertEqual(response.status_code, 200)

        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "error")
        self.assertTrue(
            'Sorry - You are not authorised' in message.message)
