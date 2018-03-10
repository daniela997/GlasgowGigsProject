import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glasgowgigs_project.settings')
import django
django.setup()
from glasgowgigs.models import Artist, Venue, Event
import datetime


def populate():
    user = []
    
    artists = [
        {"name": "Shogun", "genre": "hip-hop", "views": 20, "likes": 15},
        {"name": "Belle & Sebastian", "genre": "indie rock", "views": 40, "likes": 22},
        {"name": "Rustie", "genre": "electronic", "views": 32, "likes": 19}
        ]

    venues = [
        {"name": "King Tut's Wah Wah Hut",
         "address": "272A St Vincent St, Glasgow G2 5RL", "views": 45, "likes": 25},
        {"name": "Flying Duck",
         "address": "142 Renfield St, Glasgow G2 3AU", "views": 33, "likes": 22},
        {"name": "SWG3 Studio Warehouse",
         "address": "100 Eastvale Pl, Glasgow G3 8QG", "views": 37, "likes": 26}
        ]

    events = {
        "Rustie":
        {"King Tut's Wah Wah Hut" : {"date": datetime.date(2018, 3, 22), "bookings": 112, "views": 180},
         "Flying Duck" : {"date": datetime.date(2018, 3, 23), "bookings": 98, "views": 120}},
        "Shogun":
        {"SWG3 Studio Warehouse" : {"date": datetime.date(2018, 4, 2), "bookings": 122, "views": 150},
         "Flying Duck" : {"date": datetime.date(2018, 4, 4), "bookings": 93, "views": 122}},
        "Belle & Sebastian":
        {"King Tut's Wah Wah Hut" : {"date": datetime.date(2018, 4, 12), "bookings": 82, "views": 110},
         "Flying Duck" : {"date": datetime.date(2018, 3, 31), "bookings": 98, "views": 131}}
        }

    for v in venues:
        add_venue(v["name"], v["address"], v["likes"], v["views"])
		
    for a in artists:
        add_artist(a["name"], a["genre"], a["likes"], a["views"])
        if a["name"] in events.keys():
            for v in events[a["name"]].keys():
                venue = Venue.objects.get(name=v)
                artist = Artist.objects.get(name=a["name"])
                add_event(venue, artist, events[a["name"]][v]["date"], events[a["name"]][v]["bookings"], events[a["name"]][v]["views"])


##    for artist, venue_data in events.items():
##        for venue, event_data in venue_data.items():
##            add_event(venue, artist, event_data["date"], event_data["bookings"], event_data["views"])



def add_artist(name, genre, likes, views):
    a = Artist.objects.get_or_create(name=name)[0]
    a.name=name
    a.genre=genre
    a.views=views
    a.likes=likes
    a.save()
    return a

def add_venue(name, address, views, likes):
    v = Venue.objects.get_or_create(name=name)[0]
    v.name = name
    v.address = address
    v.views = views
    v.likes = likes
    v.save()
    return v

def add_event(venue, artist, date, bookings, views):
    e = Event.objects.get_or_create(venue=venue, artist=artist, date=date)[0]
    e.date = date
    e.views = views
    e.bookings = bookings
    e.save()
    return e

# Start execution here!
if __name__ == '__main__':
    print("Starting GlasgowGigs population script...")
    populate()
        

        
