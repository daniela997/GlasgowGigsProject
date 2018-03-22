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

    # Test with no population script 
    def test_artist_content_empty(self):
        self.assertEqual(True, True)
        c = Client()
        response = c.get('/artists', follow=True)
        response.status_code
        print("Artist content", response.content)
        print("Artist status_code", response.status_code)

    # Test if there is no video
    # def test_artist_youtube_video(self):

# Tests in case of no population script
class VenueTestCase(TestCase):

    def setUp(self):
        self.c = Client()

    # Test with no population script 
    def test_venue_content_empty(self):
        self.assertEqual(True, True)
        c = Client()
        response = c.get('/artists', follow=True)
        response.status_code
        print("Venue content", response.content)
        print("Venue status_code", response.status_code)
        
        
# Tests in case of no population script
class EventTestCase(TestCase):

    def setUp(self):
        self.c = Client()

    # Test with no population script 
    def test_event_content_empty(self):
        self.assertEqual(True, True)
        c = Client()
        response = c.get('/artists', follow=True)
        response.status_code
        print("Event content", response.content)
        print("Event status_code", response.status_code)
        
        
        
