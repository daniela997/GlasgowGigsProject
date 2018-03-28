# coding=utf-8
# To Run: populate populate_glasgowgigs.py

import os, sys
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glasgowgigs_project.settings')
django.setup()
from glasgowgigs.models import Artist, Venue, Event, UserProfile
from django.contrib.auth.models import Group, User, Permission
import datetime
from django.core.files.images import ImageFile
from embed_video.backends import detect_backend
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glasgowgigs_project.settings')
from django.contrib.contenttypes.models import ContentType


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
         "info": "Mogwai (/ˈmɒɡwaɪ/) are a Scottish post-rock band, formed in 1995 in Glasgow. The band consists of Stuart Braithwaite (guitar, vocals), Barry Burns (guitar, piano, synthesizer, vocals), Dominic Aitchison (bass guitar), and Martin Bulloch (drums). The band typically compose lengthy guitar-based instrumental pieces that feature dynamic contrast, melodic bass guitar lines, and heavy use of distortion and effects. The band were for several years signed to Glasgow label Chemikal Underground, and have been distributed by different labels such as Matador in the US and Play It Again Sam in the UK, but now use their own label Rock Action Records in the UK, and Sub Pop in North America."},
        {"name": "Franz Ferdinand", "genre": "indie rock", "views": 60, "likes": 50,
         "youtube": "https://www.youtube.com/channel/UCrvJwuMaOeKg1Rb062glUJQ",
         "instagram": "https://www.instagram.com/franz_ferdinand/",
         "soundcloud": "https://soundcloud.com/franzferdinand",
         "facebook": "https://www.facebook.com/officialfranzferdinand/",
         "twitter": "https://twitter.com/Franz_Ferdinand?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor",
         "photo": "franzferdinand.jpg",
         "video": "https://www.youtube.com/watch?v=LiyXjHEN_XA",
         "info": "Franz Ferdinand are a Scottish indie rock band, formed in 2002 and based in Glasgow. The band's original lineup was composed of Alex Kapranos (lead vocals and guitar, keyboard), Nick McCarthy (rhythm guitar, keyboards and backing vocals), Bob Hardy (bass guitar), and Paul Thomson (drums, percussion and backing vocals). Julian Corrie (keyboards, synthesiser, guitar and backing vocals) and Dino Bardot (guitar and backing vocals) joined the band in 2017 after McCarthy left during the previous year. The band has been notable for being one of the more popular post-punk revival bands, garnering multiple UK top 20 hits.[1] They have been nominated for several Grammy Awards and have received two Brit Awards – winning one for Best British Group – as well as one NME Award."},
        {"name": "Snow Patrol", "genre": "rock", "views": 45, "likes": 30,
         "youtube": "https://www.youtube.com/user/snowpatrol",
         "instagram": "https://www.instagram.com/snowpatrol/",
         "soundcloud": "https://soundcloud.com/snowpatrol",
         "facebook": "https://www.facebook.com/SnowPatrol/",
         "twitter": "https://twitter.com/snowpatrol",
         "photo": "snowpatrol.jpg",
         "video": "https://www.youtube.com/watch?v=GemKqzILV4w",
         "info": "Snow Patrol are a Northern Irish-Scottish rock band formed in 1993,[1] consisting of Gary Lightbody (vocals, guitar), Nathan Connolly (guitar, backing vocals), Paul Wilson (bass guitar, backing vocals), Jonny Quinn (drums), and Johnny McDaid (piano, guitar, backing vocals).Initially an indie rock band, the band rose to prominence in the early-mid 2000s as part of the post-Britpop movement."},
        {"name": "The Jesus and Mary Chain", "genre": "alternative rock", "views": 35, "likes": 20,
         "youtube": "https://www.youtube.com/channel/UCAlP0LcJ_RVqLvNr78w8MmA",
         "instagram": "https://www.instagram.com/jesusandmarychain/?hl=en",
         "soundcloud": "https://soundcloud.com/thejesusandmarychain",
         "facebook": "https://www.facebook.com/JesusAndMaryChain/",
         "twitter": "https://twitter.com/themarychain",
         "photo": "thejesusandmarychain.jpg",
         "video": "https://www.youtube.com/watch?v=7EgB__YratE",
         "info": "The Jesus and Mary Chain are a Scottish alternative rock band formed in East Kilbride in 1983. The band revolves around the songwriting partnership of brothers Jim and William Reid. After signing to independent label Creation Records, they released their first single 'Upside Down' in 1984. Their debut album Psychocandy was released to critical acclaim in 1985 on major label WEA. The band went on to release five more studio albums before disbanding in 1999. They reunited in 2007."},
        {"name": "Rustie", "genre": "electronic", "views": 52, "likes": 31,
         "youtube": "https://www.youtube.com/channel/UCs2exSrWeaiCnrmJk_YzBHw",
         "instagram": "https://www.instagram.com/rustie432/",
         "soundcloud": "https://soundcloud.com/rustie",
         "facebook": "",
         "twitter": "https://twitter.com/rustie",
         "photo": "rustie.jpg",
         "video": "https://www.youtube.com/watch?v=s4AqCrR_nAU",
         "info": "Glasgow’s Russell Whyte is behind some of the most joyous, hyperactive, and truly original club music of recent years. As electronic alchemist Rustie, he harnesses the energy and euphoria of hyphy hip-hop and trance, spikes it with speaker-mangling bass and flashes of techno and channels this all into intense dancefloor detonators, a sound he honed playing at nights thrown by local label collectives Numbers and LuckyMe."},
        {"name": "Jackmaster", "genre": "house", "views": 48, "likes": 39,
         "youtube": "",
         "instagram": "https://www.instagram.com/jackmaster/",
         "soundcloud": "https://soundcloud.com/jackmaster",
         "facebook": "https://www.facebook.com/djjackmaster/",
         "twitter": "https://twitter.com/jackmaster",
         "photo": "jackmaster.jpg",
         "video": "https://www.youtube.com/watch?v=zVinzVxXHpY",
         "info":"Jack Revill, better known as Jackmaster, (born 11 January 1986) is a Scottish DJ from Glasgow. He is a co-founder of the record label and club night Numbers as well as Wireblock, Dress 2 Sweat and Point.One Recordings. He is renowned for his in-depth and diverse music taste and ability to mix a multitude of different genres as well as being one of a few examples of a DJ known primarily as a DJ (rather than a producer), alongside Hessle Audio’s Ben UFO and Rinse FM’s Oneman"},
        {"name": "Boards of Canada", "genre": "electronica", "views": 40, "likes": 33,
         "youtube": "https://www.youtube.com/channel/UC9D7VN2HldiRFdxFvCcyA7A",
         "instagram": "https://www.instagram.com/boards_of_canada/",
         "soundcloud": "https://soundcloud.com/boardsofcanada",
         "facebook": "https://www.facebook.com/boardsofcanada/",
         "twitter": "https://twitter.com/boctransmission",
         "photo": "boardsofcanada.jpg",
         "video": "https://www.youtube.com/watch?v=XaJn3QqiIUc",
         "info": "Boards of Canada are a Scottish electronic music duo consisting of brothers Michael Sandison and Marcus Eoin.[2][3] Signing to Skam and then Warp Records in the 1990s, the duo received recognition following the release of their influential debut album Music Has the Right to Children in 1998.They have since released subsequent recordings to critical praise, including Geogaddi (2002) and Tomorrow's Harvest (2013), and have remained reclusive, rarely giving interviews or performing live. The music of Boards of Canada incorporates elements such as vintage analogue synthesisers, hip hop-inspired breakbeats, and samples from 1970s public broadcasting programmes and other outdated media; it has been described as exploring themes of nostalgia, childhood memory, and nature. In 2012, FACT called them 'one of the best-known and best-loved electronic acts of the last two decades.'"},
        {"name": "Kode9", "genre": "electronic", "views": 36, "likes": 27,
         "youtube": "",
         "instagram": "https://www.instagram.com/kode9/",
         "soundcloud": "https://soundcloud.com/kodenine",
         "facebook": "https://www.facebook.com/djkode9/",
         "twitter": "https://twitter.com/kodenine",
         "photo": "kode9.jpg",
         "video": "https://www.youtube.com/watch?v=Pr6d2KQEcy8",
         "info": "Steve Goodman, known as Kode9 (born 1973) is a Glasgow-born, London-based electronic music artist, DJ, and founder of the Hyperdub record label.[1] Initially inspired by what he calls the 'hardcore continuum' of British dance music, he was one of the founding members of the early dubstep scene with the late MC and former collaborator The Spaceape. He has released three full-length albums: Memories of the Future (2006) and Black Sun (2011), both with The Spaceape, and Nothing (2015). As owner of Hyperdub, Goodman has signed artists such as Burial, DJ Rashad, Zomby, and Fatima Al Qadiri. Goodman has a Ph.D. in philosophy from the University of Warwick and has published a book, Sonic Warfare: Sound, Affect, and the Ecology of Fear."},
        {"name": "Calvin Harris", "genre": "EDM", "views": 67, "likes": 48,
         "youtube": "https://www.youtube.com/channel/UCaHNFIob5Ixv74f5on3lvIw",
         "instagram": "https://www.instagram.com/calvinharris/",
         "soundcloud": "https://soundcloud.com/calvinharris",
         "facebook": "https://www.facebook.com/calvinharris",
         "twitter": "https://twitter.com/CalvinHarris",
         "photo": "calvinharris.jpg",
         "video": "https://www.youtube.com/watch?v=ebXbLfLACGM",
         "info": "Adam Richard Wiles (born 17 January 1984), known professionally as Calvin Harris, is a Scottish DJ, singer, songwriter, and record producer. His debut studio album I Created Disco was released in June 2007 and it spawned two UK top 10 singles 'Acceptable in the 80s' and 'The Girls'. In 2009, Harris released his second studio album Ready for the Weekend, which debuted at number one on the UK Albums Chart and was later certified gold by the British Phonographic Industry within two months of its release. Its lead single 'Im Not Alone' became his first song to top the UK Singles Chart.Harris rose to international prominence with the release of his third studio album 18 Months in October 2012. Topping the UK charts, the album became his first to chart on the US Billboard 200 chart (where it reached number 19). All eight of the albums singles, which were 'Bounce', 'Feel So Close', 'Lets Go', 'Well Be Coming Back', 'Sweet Nothing', 'Drinking from the Bottle', 'I Need Your Love' and 'Thinking About You' reached the top 10 in the UK. At the time, Harris broke the record for the most top 10 songs from one studio album on the UK Singles Chart with eight entries, surpassing Michael Jackson. Harris released his fourth studio album Motion in November 2014. It debuted at number two in the UK and at number five in the US and became Harris second consecutive number one album on the US Dance/Electronic Albums chart. The albums first three singles 'Under Control', 'Summer' and 'Blame' all topped the UK chart."}
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
        {"name": "La Cheetah",
         "address": "73 Queen St, Glasgow G1 3BZ", "views": 32, "likes": 25,
         "photo": "lacheetah.jpg", "latitude": 55.859500, "longitude": -4.252127,
         "info": "Named after a famous salsa club, La Cheetah is situated in the basement of Max's in Glasgow's Merchant City. The tiny venue is accessed through the same doors as the public entrance. A small room with a bar, the DJ booth dominates the space. La Cheetah's limited capacity often offers the opportunity to see some of the biggest names in electronic music in an especially intimate environment.",
         "instagram": "https://www.instagram.com/lacheetahclub/", "twitter": "https://twitter.com/LaCheetahClub", "facebook": "https://www.facebook.com/lacheetahclub"},
        {"name": "The Art School",
         "address": "20 Scott St, Glasgow G3 6PE", "views": 40, "likes": 36,
         "photo": "theartschool.png", "latitude": 55.866488, "longitude": -4.264228,
         "info": "The Art School is a student and artist led venue in Glasgow. We offer space and support for a wide range of artistic and musical practices, hosting gigs, clubs, films and educational events, alongside the regular opening hours of our core social and dining facilities in the Vic Café Bar. As a non-profit charity, all proceeds made by The Art School go towards funding student exhibitions, projects, and societies, along with contributing to our ‘Programming Fund’ for innovative and emerging artists and events. We are supported by both the Glasgow School of Art and our own commercial activities, and in turn work as a representative body for students at the GSA, advocating for their interests and welfare. With a building comprised of several mouldable Project Spaces, a large multifunctional Assembly Hall and well-loved Vic Café Bar, our facilities offer a range of opportunities and resources: helping our communities learn and share skills in ways beyond traditional canons, classrooms and lecture theatres. We try to make everybody feel comfortable and welcome in the venue, and have an on-going and self-critical commitment to accessibility, safe(r) spaces and actively opposing all forms of discrimination.",
         "instagram": "", "twitter": "https://twitter.com/theartskl", "facebook": "https://www.facebook.com/theartskl/"},
        {"name": "Barrowland Ballroom",
         "address": "244 Gallowgate, Glasgow G4 0TT", "views": 67, "likes": 53,
         "photo": "barrowlandballroom.jpg", "latitude": 55.855338, "longitude": -4.236775,
         "info": "The famous Barrowlands maybe isn't quite as busy with bookings as it once was, with competition stiff from the similarly-sized, corporate-sponsored ABC and Academy venues, but the best bands know this dusty old 1960s ballroom is a must-play, given the chance. Think mid-sized indie and rock touring bands in the main, often of a certain vintage and/or high critical cache – the likes of My Bloody Valentine, Arcade Fire and Pixies have all played within the last year. Oasis and Metallica are just two among many bands to have described it as one of their favourite venues in the world. Bowie even visited the Barrowland back in 1997, taking a fallen ceramic star from the ceiling away with him as a souvenir. Oh, and Stiff Little Fingers play every St Patrick's Day.",
         "instagram": "https://www.instagram.com/the_barrowlands/", "twitter": "https://twitter.com/thebarrowlands", "facebook": ""},
        {"name": "Broadcast",
         "address": "427 Sauchiehall St, Glasgow G2 3LG", "views": 45, "likes": 38,
         "photo": "broadcast.jpg", "latitude": 55.866049, "longitude": -4.269132,
         "info": "Broadcast – situated much more centrally, practically eyeball-to-eyeball with nearest rival Nice 'n' Sleazy. Owners PCL, one of Scotland’s biggest concert promoters, have sagely let the kitchen out as a franchise, run by Sean Toner – previously at Crabshakk and many other Glasgow eateries before that. Realistic about the limited range of demand for good food on Sauchiehall St, he’s doing ambitious things within the narrow confines of pub grub – pizzas with Mediterranean toppings (up to two-feet large), homemade burgers from high-quality Andrew Reid beef and healthy, zesty salads. Most of the food and drink will be wolfed down pre or post gig but it may in time become as hot a ticket as the near-nightly shows downstairs.",
         "instagram": "https://www.instagram.com/broadcastglasgow/", "twitter": "https://twitter.com/BroadcastGLA", "facebook": "https://www.facebook.com/broadcastglasgow/"},
        {"name": "O2 ABC",
         "address": "300 Sauchiehall Street, Glasgow G2 3JA", "views": 30, "likes": 25,
         "photo": "O2ABC.jpg", "latitude": 55.865741, "longitude": -4.264184,
         "info": "Initially called the plain-old ABC when it opened as a music and club venue in 2005 after a £2 million conversion (it’s been a cinema, hippodrome and ice-rink since being built in the 1920s) the potential for this Sauchiehall Street art deco building was recognised by Regular Music. In 2009, the Academy Music Group, owners of the O2 Academy and many other venues nationwide, bought a majority stake in the business, bringing in corporate-sponsored rebranding, and solidifying the O2’s status as Scotland’s key mid-level music venue.",
         "instagram": "https://www.instagram.com/o2abc/", "twitter": "https://twitter.com/O2ABC", "facebook": "https://www.facebook.com/o2abcglasgow/"},
        {"name": "Centre of Contemporary Arts",
         "address": "350 Sauchiehall St, Glasgow G2 3JD", "views": 32, "likes": 26,
         "photo": "CCA.jpg", "latitude": 55.865769, "longitude": -4.265164,
         "info": "CCA: Centre for Contemporary Arts is Glasgow’s hub for the arts. Our year-round programme includes cutting-edge exhibitions, film, music, literature, spoken word, festivals, Gaelic and performance. At the heart of all activities is the desire to work with artists, commission new projects and present them to the widest possible audience.",
         "instagram": "https://www.instagram.com/cca_glasgow/", "twitter": "https://twitter.com/CCA_Glasgow", "facebook": "https://www.facebook.com/CCA.Glasgow.1"},
        {"name": "SSE Hydro",
         "address": "Exhibition Way, Glasgow G3 8YW", "views": 63, "likes": 42,
         "photo": "SSEHydro.jpg", "latitude": 55.860206, "longitude": -4.285263,
         "info": "The massive, flying saucer-like SSE Hydro is the latest unmissable architectural landmark to be added to the now vast arena precinct by the banks of the Clyde. Opened in 2013 with a capacity of 13,000, it joined the 1980s-built SECC (Scottish Exhibition and Conference Centre, max capacity 10,000) and 1990s-built Clyde Auditorium (or ‘the Armadillo’ as its known, capacity 3,000), and immediately plugged a big, sub-stadium gap in live music and entertainment in Glasgow. Beyoncé, Miley Cyrus, Black Sabbath and Prince all played The Hydro within its first year while major events there have included the MOBO Awards, MTV Europe Music Awards and Ryder Cup gala concert.",
         "instagram": "https://www.instagram.com/thessehydro/?hl=en", "twitter": "https://twitter.com/TheSSEHydro", "facebook": "https://www.facebook.com/thehydro/"},
        {"name": "Sub Club",
         "address": "22 Jamaica St, Glasgow G1 4QD", "views": 46, "likes": 33,
         "photo": "subclub.jpg", "latitude": 55.858045, "longitude": -4.257453,
         "info": "Glasgow's Sub Club is arguably Scotland's most famous electronic music venue. First opened in April 1987, the Jamaica Street club has been home to residents Harri & Domenic's Subculture party since 1994, and famously hosted JD Twitch and JG Wilkes' Optimo (Espacio) event every Sunday from 1997 to 2010. Sub Club was also an early home to Glasgow techno favourites Slam. In 2006 the club installed one of the UK's largest bodysonic dance floors. More recently promoters such as Numbers and Sensu have been regulars at the venue. House, techno, electro, disco, bass music and many other genres are regularly found there.",
         "instagram": "", "twitter": "https://twitter.com/SubClub?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor", "facebook": "https://www.facebook.com/subclub/"}
        ]

    events = {
        "Mogwai":
            {"King Tut's Wah Wah Hut" : {"date": datetime.date(2018, 3, 22), "bookings": 112, "views": 180},
             "Flying Duck" : {"date": datetime.date(2018, 3, 23), "bookings": 98, "views": 120}},
        "Shogun":
            {"SWG3 Studio Warehouse" : {"date": datetime.date(2018, 4, 2), "bookings": 122, "views": 150},
             "Flying Duck" : {"date": datetime.date(2018, 6, 4), "bookings": 93, "views": 122}},
        "Belle & Sebastian":
            {"King Tut's Wah Wah Hut" : {"date": datetime.date(2018, 8, 12), "bookings": 82, "views": 110},
             "Flying Duck" : {"date": datetime.date(2018, 3, 31), "bookings": 98, "views": 131}},
        "Franz Ferdinand":
            {"O2 ABC" : {"date": datetime.date(2018, 3, 20), "bookings": 122, "views": 210},
             "La Cheetah": {"date": datetime.date(2018, 7, 14), "bookings": 78, "views": 96}},
        "Snow Patrol":
            {"Sub Club": {"date": datetime.date(2018, 8, 20), "bookings": 109, "views": 140},
             "Barrowland Ballroom": {"date": datetime.date(2018, 4, 16), "bookings": 23, "views": 57},
             "The Art School": {"date": datetime.date(2018, 5, 30), "bookings": 45, "views": 86}},
        "The Jesus and Mary Chain":
             {"Centre of Contemporary Arts": {"date": datetime.date(2018, 4, 20), "bookings": 78, "views": 105},
              "Flying Duck": {"date": datetime.date(2018, 3, 15), "bookings": 138, "views": 204}},
        "Rustie":
            {"SSE Hydro": {"date": datetime.date(2018, 5, 23), "bookings": 305, "views": 432},
             "Barrowland Ballroom": {"date": datetime.date(2018, 5, 5), "bookings": 139, "views": 177},
             "King Tut's Wah Wah Hut": {"date": datetime.date(2018, 6, 20), "bookings": 166, "views": 189}},
        "Boards of Canada":
            {"Centre of Contemporary Arts": {"date": datetime.date(2018, 7, 12), "bookings": 47, "views": 66},
             "Flying Duck": {"date": datetime.date(2018, 5, 24), "bookings": 102, "views": 154}},
        "Kode9":
            {"O2 ABC": {"date": datetime.date(2018, 5, 15), "bookings": 76, "views": 116}},
        "Calvin Harris":
            {"SSE Hydro": {"date": datetime.date(2018, 8, 20), "bookings": 1367, "views": 983}},
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

    groups = [ "VenueOwners", "ArtistManagers"]

    for g in groups:
        g, created = Group.objects.get_or_create(name=g)
    for g in groups:
        if g == "VenueOwners":
            group = Group.objects.get(name=g)

            permission = Permission.objects.get(codename='perm_add_venue')
            group.permissions.add(permission)

            permission = Permission.objects.get(codename='perm_add_event')
            group.permissions.add(permission)


            
        if g == "ArtistManagers":
            group = Group.objects.get(name=g)
            
            permission = Permission.objects.get(codename='perm_add_artist')
            group.permissions.add(permission)
            
            permission = Permission.objects.get(codename='perm_add_event')
            group.permissions.add(permission)         

    

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
