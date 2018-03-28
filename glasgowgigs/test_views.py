from django.test import TestCase
from glasgowgigs.views import Artist
from django.test import Client
from django.core.urlresolvers import reverse
from django.http import HttpRequest
from django.urls import resolve

class IndexPageTests(TestCase):

    # Test homepage returns an HTTP 200 status code
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # Test that the index page uses the index and base templates
    def test_index_using_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'glasgowgigs/index.html', 'glasgowgigs/base.html')

    """
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = IndexView(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>GlasgowGigs</title>', html)
        self.assertTrue(html.endswith('</html>'))
        """

    def test_index_shows_number_of_artists(self):
        # Access artist
        try:
            response = self.client.get(reverse('artist'))
        except:
            try:
                response = self.client.get(reverse('glasgowgigs:artist'))
            except:
                return False
        # Check if it contains views message
        self.assertIn('views: 1'.lower(), response.content.decode('ascii').lower())

    # Test artist detail page created
    # Test Like button function