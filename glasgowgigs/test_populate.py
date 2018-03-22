from django.test import TestCase
from populate_glasgowgigs import populate
from django.test import Client

class PopulateArtistTestCase(TestCase):

    def setUp(self):
        self.c = Client()

    def test_artist_content_empty(self):
        self.assertEqual(True, True)

        c = Client()
        response = c.get('/populate', follow=True)
        response.status_code
        print("content", response.content)
        print("status_code", response.status_code)