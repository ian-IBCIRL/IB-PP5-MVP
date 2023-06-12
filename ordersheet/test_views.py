from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse
from ordersheet.views import add_to_ordersheet, adjust_ordersheet


class ordersheetViewsTests(TestCase):
    """ test ordersheet views and functions work """
    fixtures = ['May23datadump.json', 'categories.json']  # set up test data

    def test_ordersheet_list_view(self):
        resp = self.client.get(reverse('ordersheet'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name='ordersheet/ordersheet.html')  # noqa

    def test_add_to_ordersheet_view(self):
        resp = self.client.get(reverse('ordersheet'))
        self.assertEqual(resp.status_code, 200)

    def test_add_item_qty_size_to_add_ordersheet_views(self):
        resp = self.client.post(
            '/ordersheet/add/1/', {'quantity': '7', 'redirect_url': 'ordersheet'})  # noqa
        messages = list(get_messages(resp.wsgi_request))
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         'Added Information Security Policy to your ordersheet')   # noqa

    def test_add_item_qty_to_add_ordersheet_views(self):
        resp = self.client.post(
            '/ordersheet/add/2/', {'quantity': '4', 'redirect_url': 'ordersheet', })  # noqa
        messages = list(get_messages(resp.wsgi_request))
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         'Added Data Protection Policy to your ordersheet')

    def test_add_item_qty_size_to_adjust_ordersheet_views(self):
        resp = self.client.post(
            '/ordersheet/adjust/1/', {'quantity': '7'})
        messages = list(get_messages(resp.wsgi_request))
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "Updated Information Security Policy quantity to 7")
