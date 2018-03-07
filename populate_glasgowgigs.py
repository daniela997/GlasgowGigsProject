import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glasgowgigs_project.settings')
import django
django.setup()
from glasgowgigs.models import Artist, Venue, Event

def populate():
    artists = [
        {"name": "Shogun"},
        {"name": "Zombie"},
        {"name": "Belle & Sebastian"},
        {"name": "Rustie"}
        ]

    venues = [
        {"name": "King Tut's Wah Wah Hut",
         "address": "@55.862629,-4.265005,15z"},
        {"name": "Flying Duck",
         "address": "@55.8655041,-4.2550565,15z"},
        {"name": "SWG3 Studio Warehouse",
         "address": "@55.864523,-4.299685,15z"}
        ]
    events = [
        ]
        

        
