# -*- coding: utf-8 -*-
import os, sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glasgowgigs_project.settings')
import django
django.setup()
from glasgowgigs.models import Artist, Venue, Event
import datetime
from django.core.files.images import ImageFile



def populate():
    
    
    artists = [
        {"name": "Shogun", "genre": "hip-hop", "views": 20, "likes": 15,
         "youtube": "https://www.youtube.com/channel/UC3IizCaGplXl7CWw1hKzHYg",
         "instagram": "https://www.instagram.com/shogun_mftm/",
         "soundcloud": "https://soundcloud.com/shogun_official",
         "facebook": "https://www.facebook.com/Shogun.MFTM/",
         "twitter": "https://twitter.com/shogan_sama",
         "photo": 'shogun.jpg',
         "info": "Shogun is a 19 year-old rapper from Paisley, Scotland. He drew attention when the video for the song “Vulcan” went viral and gained over a million views on YouTube."},
        {"name": "Belle & Sebastian", "genre": "indie rock", "views": 40, "likes": 22,
         "youtube": "https://www.youtube.com/channel/UClz7tzOxFJT_v5iOfh8PPvg",
         "instagram": "https://www.instagram.com/bellesglasgow/",
         "soundcloud": "https://soundcloud.com/belle-and-sebastian",
         "facebook": "https://www.facebook.com/belleandsebastian/",
         "twitter": "https://twitter.com/bellesglasgow/",
         "photo": 'belleandsebastian.jpg',
         "info": "Belle and Sebastian are a Scottish band formed in Glasgow in January 1996. Led by Stuart Murdoch, the band has released 9 albums to date. Much of their work had been released on Jeepster Records, but they are now signed to Rough Trade Records in the United Kingdom and Matador Records in the United States. Though often praised by critics, Belle and Sebastian have enjoyed only limited commercial success."},
        {"name": "Mogwai", "genre": "post rock", "views": 32, "likes": 19,
         "youtube": "https://www.youtube.com/channel/UCqEG1Kwq26Zv2JfqdAwj9kg",
         "instagram": "https://www.instagram.com/mogwaiband/",
         "soundcloud": "https://soundcloud.com/mogwai-official",
         "facebook": "https://www.facebook.com/mogwai/",
         "twitter": "https://twitter.com/mogwaiband",
         "photo": 'mogwai.jpg',
         "info": "Mogwai (/ˈmɒɡwaɪ/) are a Scottish post-rock band, formed in 1995 in Glasgow. The band consists of Stuart Braithwaite (guitar, vocals), Barry Burns (guitar, piano, synthesizer, vocals), Dominic Aitchison (bass guitar), and Martin Bulloch (drums). The band typically compose lengthy guitar-based instrumental pieces that feature dynamic contrast, melodic bass guitar lines, and heavy use of distortion and effects. The band were for several years signed to Glasgow label Chemikal Underground, and have been distributed by different labels such as Matador in the US and Play It Again Sam in the UK, but now use their own label Rock Action Records in the UK, and Sub Pop in North America. "}
        ]

    venues = [
        {"name": "King Tut's Wah Wah Hut",
         "address": "272A St Vincent St, Glasgow G2 5RL", "views": 45, "likes": 25,
         "photo": 'kingtuts.jpg', "latitude": '55.862629', "longitude": '-4.265005'},
        {"name": "Flying Duck",
         "address": "142 Renfield St, Glasgow G2 3AU", "views": 33, "likes": 22,
         "photo": 'flyingduck.jpg', "latitude": '55.8655041', "longitude": '-4.2550565'},
        {"name": "SWG3 Studio Warehouse",
         "address": "100 Eastvale Pl, Glasgow G3 8QG", "views": 37, "likes": 26,
         "photo": 'swg3.jpg', "latitude": '55.864523', "longitude": '-4.299685'},
        ]

    events = {
        "Mogwai":
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
        add_venue(v["name"], v["address"], v["likes"], v["views"], v["photo"], v["latitude"], v["longitude"])
		
    for a in artists:
        add_artist(a["name"], a["genre"], a["likes"], a["views"], a["youtube"], a["instagram"], a["soundcloud"], a["twitter"], a["facebook"], a["info"], a["photo"])
        if a["name"] in events.keys():
            for v in events[a["name"]].keys():
                venue = Venue.objects.get(name=v)
                artist = Artist.objects.get(name=a["name"])
                add_event(venue, artist, events[a["name"]][v]["date"], events[a["name"]][v]["bookings"], events[a["name"]][v]["views"])




##    for artist, venue_data in events.items():
##        for venue, event_data in venue_data.items():
##            add_event(venue, artist, event_data["date"], event_data["bookings"], event_data["views"])



def add_artist(name, genre, likes, views, youtube, instagram, soundcloud, twitter, facebook, info, photo):
    a = Artist.objects.get_or_create(name=name)[0]
    a.name=name
    a.genre=genre
    a.views=views
    a.likes=likes
    a.youtube = youtube
    a.instagram = instagram
    a.soundcloud = soundcloud
    a.twitter = twitter
    a.facebook = facebook
    a.info = info
    a.photo = ImageFile(open(photo, "rb"))      
    a.save()
    return a

def add_venue(name, address, views, likes, photo, latitude, longitude):
    v = Venue.objects.get_or_create(name=name)[0]
    v.name = name
    v.address = address
    v.views = views
    v.likes = likes
    v.photo = ImageFile(open(photo, "rb"))   
    v.latitude = latitude
    v.longitude = longitude 
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
        

        
