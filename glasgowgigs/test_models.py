# To Run the test:
# python manage.py test
# Clear population script first

from django.test import TestCase
from glasgowgigs.models import Artist, Venue, Event
from django.test import Client

# Tests in case of no population script
class ArtistTestCase(TestCase):

    def setUp(self):
        #Artist.objects.create()
        self.c = Client()

    def test_artist_content_empty(self):
        self.assertEqual(True, True)

        c = Client()
        response = c.get('/artists', follow=True)
        response.status_code
        print("content", response.content)
        print("status_code", response.status_code)

# Test if there is no video

# Tests in case of no population script
class VenuesTestCase(TestCase):

    def setUp(self):
        self.c = Client()

    def test_venues_content_empty(self):
        self.assertEqual(True, True)

        c = Client()
        response = c.get('/artists', follow=True)
        response.status_code
        print("content", response.content)
        print("status_code", response.status_code)
        
        
# Tests in case of no population script
class EventsTestCase(TestCase):

    def setUp(self):
        self.c = Client()

    def test_events_content_empty(self):
        self.assertEqual(True, True)

        c = Client()
        response = c.get('/artists', follow=True)
        response.status_code
        print("content", response.content)
        print("status_code", response.status_code)
        
        
        
