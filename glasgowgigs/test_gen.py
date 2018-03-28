from django.test import TestCase
from django.contrib.staticfiles import finders

# To Run the test:
# python manage.py test


class GeneralTests(TestCase):

    # Test to establish that tests are working
    def test_basic_addition(self):
        self.assertEqual(2 + 2, 4)

    # If using static media correctly the result is not NONE
    def test_static_files(self):
        result = finders.find('images/logo.png')
        self.assertIsNotNone(result)

    # Test homepage returns an HTTP 200 status code (responds)
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
