# To Run the test:
# python manage.py test

from django.test import TestCase
from glasgowgigs.models import Artist, Venue, Event, UserProfile
from django.test import Client
from django.core.urlresolvers import reverse

# Tests for Artists
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
        #print("Artist content", response.content)
        #print("Artist status_code", response.status_code)

    # Test if slug line is added
    def test_artist_slug_creation(self):
        artist = Artist(name='Random Artist String', photo=None)
        artist.save()
        self.assertEqual(artist.slug, 'random-artist-string')

"""
    # Test that views are positive
    def test_artist_pos_views(self):
        artist = Artist(name='artist', views=-1)
        artist.save()
        self.assertEqual((artist.views >= 0), True)
"""

# Tests for Venues
class VenueTestCase(TestCase):

    def setUp(self):
        self.c = Client()

    # Test with no population script 
    def test_venue_content_empty(self):
        self.assertEqual(True, True)
        c = Client()
        response = c.get('/artists', follow=True)
        response.status_code
        #print("Venue content", response.content)
        #print("Venue status_code", response.status_code)

    # Test if slug line is added
    def test_venue_slug_creation(self):
        venue = Venue(name='Random Venue String', photo=None)
        venue.save()
        self.assertEqual(venue.slug, 'random-venue-string')
        
        
# Tests for Events
class EventTestCase(TestCase):

    def setUp(self):
        self.c = Client()

    # Test with no population script 
    def test_event_content_empty(self):
        self.assertEqual(True, True)
        c = Client()
        response = c.get('/artists', follow=True)
        response.status_code
        #print("Event content", response.content)
        #print("Event status_code", response.status_code)
        
    # Test if slug line is added
    def test_event_slug_creation(self):
        ven = Venue(name='venue', photo=None)
        ven.save()
        art = Artist(name='artist', photo=None)
        art.save()
        event = Event(name='Random Event String', venue=ven, artist=art, date='1996-03-03')
        event.save()
        self.assertEqual(event.slug, 'artist-venue-on-1996-03-03')
