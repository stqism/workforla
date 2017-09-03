from django.test import Client
from django.test import TestCase


class HomepageTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_homepage_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Work For LA',
                      response.content.decode(response.charset))
