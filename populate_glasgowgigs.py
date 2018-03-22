# coding=utf-8
# To Run: populate populate_glasgowgigs.py

import os, sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glasgowgigs_project.settings')
import django
django.setup()
from glasgowgigs.models import Artist, Venue, Event
import datetime
from django.core.files.images import ImageFile
from embed_video.backends import detect_backend




def populate():
    
    
    artists = [
        {"name": "Shogun", "genre": "hip-hop", "views": 20, "likes": 15,
         "youtube": "https://www.youtube.com/channel/UC3IizCaGplXl7CWw1hKzHYg",
         "instagram": "https://www.instagram.com/shogun_mftm/",
         "soundcloud": "https://soundcloud.com/shogun_official",
         "facebook": "https://www.facebook.com/Shogun.MFTM/",
         "twitter": "https://twitter.com/shogan_sama",
         "photo": 'shogun.jpg',
         "video": 'https://www.youtube.com/watch?v=2ZOAzbH8tdU',
         "info": "Shogun is a 19 year-old rapper from Paisley, Scotland. He drew attention when the video for the song “Vulcan” went viral and gained over a million views on YouTube."},
        {"name": "Belle & Sebastian", "genre": "indie rock", "views": 40, "likes": 22,
         "youtube": "https://www.youtube.com/channel/UClz7tzOxFJT_v5iOfh8PPvg",
         "instagram": "https://www.instagram.com/bellesglasgow/",
         "soundcloud": "https://soundcloud.com/belle-and-sebastian",
         "facebook": "https://www.facebook.com/belleandsebastian/",
         "twitter": "https://twitter.com/bellesglasgow/",
         "photo": 'belleandsebastian.jpg',
         "video": 'https://www.youtube.com/watch?v=fso8D9lgJVY',
         "info": "Belle and Sebastian are a Scottish band formed in Glasgow in January 1996. Led by Stuart Murdoch, the band has released 9 albums to date. Much of their work had been released on Jeepster Records, but they are now signed to Rough Trade Records in the United Kingdom and Matador Records in the United States. Though often praised by critics, Belle and Sebastian have enjoyed only limited commercial success."},
        {"name": "Mogwai", "genre": "post rock", "views": 32, "likes": 19,
         "youtube": "https://www.youtube.com/channel/UCqEG1Kwq26Zv2JfqdAwj9kg",
         "instagram": "https://www.instagram.com/mogwaiband/",
         "soundcloud": "https://soundcloud.com/mogwai-official",
         "facebook": "https://www.facebook.com/mogwai/",
         "twitter": "https://twitter.com/mogwaiband",
         "photo": 'mogwai.jpg',
         "video": 'https://www.youtube.com/watch?v=3BHmKPIeFqw',
         "info": "Mogwai (/ˈmɒɡwaɪ/) are a Scottish post-rock band, formed in 1995 in Glasgow. The band consists of Stuart Braithwaite (guitar, vocals), Barry Burns (guitar, piano, synthesizer, vocals), Dominic Aitchison (bass guitar), and Martin Bulloch (drums). The band typically compose lengthy guitar-based instrumental pieces that feature dynamic contrast, melodic bass guitar lines, and heavy use of distortion and effects. The band were for several years signed to Glasgow label Chemikal Underground, and have been distributed by different labels such as Matador in the US and Play It Again Sam in the UK, but now use their own label Rock Action Records in the UK, and Sub Pop in North America. "}
        ]

    venues = [
        {"name": "King Tut's Wah Wah Hut",
         "address": "272A St Vincent St, Glasgow G2 5RL", "views": 45, "likes": 25,
         "photo": 'kingtuts.jpg', "latitude": 55.862629, "longitude": -4.265005,
         "info": "Since its inception in 1990, King Tut’s Wah Wah Hut has been at the forefront of the Scottish live music scene and continues to be one of the most celebrated venues in the world. King Tut’s is an exciting showcase for new and emerging bands and is the venue that supported some of the music industry's biggest names at the start of their careers: from Oasis (who were famously signed by Alan McGee at the venue in 1993) to Radiohead, The Killers, Juliette Lewis, Pulp, My Chemical Romance, Florence & The Machine, Biffy Clyro, Manic Street Preachers, Snow Patrol, Frightened Rabbit and Paolo Nutini plus many, many, more.",
         "instagram": "https://www.instagram.com/kingtutsofficial/", "twitter": "https://twitter.com/kingtuts", "facebook": "https://www.facebook.com/kingtutswahwahhut/"},
        {"name": "Flying Duck",
         "address": "142 Renfield St, Glasgow G2 3AU", "views": 33, "likes": 22,
         "photo": 'flyingduck.jpg', "latitude": 55.8655041, "longitude": -4.2550565,
         "info": "Glasgow’s best kept secret, hidden gem and fav underground haunt, The Duck combines bar, diner, late night fun, event & gig space into a chilled out and unpretentious hideout. Opening in 2007, people have been known to lose themselves for hours in the depths of this lo-fi venue/bar/whatever with a selection of board games, pub quizzes, film screenings, gigs, performances, late night dancing and, uh, anything else. Top nosh vegan diner style food served until 22hr (and 23hr on fri & sat), burgers, loaded fries, macaroni cheese and milkshake cocktails.",
         "instagram": "", "twitter": "https://twitter.com/flyduckglasgow", "facebook": "https://www.facebook.com/flyingduckparty/"},
        {"name": "SWG3 Studio Warehouse",
         "address": "100 Eastvale Pl, Glasgow G3 8QG", "views": 37, "likes": 26,
         "photo": 'swg3.jpg', "latitude": 55.864523, "longitude": -4.299685,
         "info": "SWG3 is a multi disciplinary arts venue and events company. Now one of the leading venues and locations to hire in Glasgow, the SWG3 Complex play host to a multitude of different types of events, ranging from niche product launches to global brand activation, corporate dinners, fashion shows and Food & Drink events.",
         "instagram": "https://www.instagram.com/swg3glasgow/", "twitter": "https://twitter.com/swg3glasgow", "facebook": "https://www.facebook.com/SWG3glasgow/"},
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
        add_venue(v["name"], v["address"], v["likes"], v["views"], v["photo"], v["latitude"], v["longitude"], v["info"], v["instagram"], v["twitter"], v["facebook"])
		
    for a in artists:
        add_artist(a["name"], a["genre"], a["likes"], a["views"], a["youtube"], a["instagram"], a["soundcloud"], a["twitter"], a["facebook"], a["info"], a["photo"], a["video"])
        if a["name"] in events.keys():
            for v in events[a["name"]].keys():
                venue = Venue.objects.get(name=v)
                artist = Artist.objects.get(name=a["name"])
                add_event(venue, artist, events[a["name"]][v]["date"], events[a["name"]][v]["bookings"], events[a["name"]][v]["views"])



def add_artist(name, genre, likes, views, youtube, instagram, soundcloud, twitter, facebook, info, photo, video):
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
    a.video = video    
    a.save()
    return a

def add_venue(name, address, views, likes, photo, latitude, longitude, info, instagram, twitter, facebook):
    v = Venue.objects.get_or_create(name=name)[0]
    v.name = name
    v.address = address
    v.views = views
    v.likes = likes
    v.photo = ImageFile(open(photo, "rb"))   
    v.latitude = latitude
    v.longitude = longitude
    v.info = info
    v.instagram = instagram
    v.twitter = twitter
    v.facebook = facebook
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
