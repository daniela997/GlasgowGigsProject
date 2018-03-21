from django.test import TestCase
from glasgowgigs.models import Artist
from django.test import Client

class AnimalTestCase(TestCase):

    def setUp(self):
        #Artist.objects.create()
        self.c = Client()

    def test_animals_can_speak(self):
        self.assertEqual(True, True)

        c = Client()
        response = c.get('/artists', follow=True)
        response.status_code
        print("content", response.content)
        print("status_code", response.status_code)