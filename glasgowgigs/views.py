from django.shortcuts import render
from django.http import HttpResponse
from .models import Artist, Venue, Event
from django.views import generic



def index(request):
    #context_dict = {'boldmessage': "Crunch, creamy, cookie, candy, cupcake!"}
    #return render(request, 'glasgowgigs/index.html', context=context_dict)

    # stats
    num_artists=Artist.objects.all().count()
    num_venues=Venue.objects.all().count()
    num_events=Event.objects.all().count()

    #events during the current month
    #coming_soon_events=Event.objects.filter(date.month=today.month).count()
    
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'glasgowgigs/index.html',
        context={'num_artists':num_artists,'num_venues':num_venues,'num_events':num_events},
    )

def about(request):
    context_dict = {}
    return render(request, 'glasgowgigs/about.html', context=context_dict)

def artists(request):
    context_dict = {}
    return render(request, 'glasgowgigs/artists.html', context=context_dict)

def venues(request):
    context_dict = {}
    return render(request, 'glasgowgigs/venue.html', context=context_dict)


class ArtistListView(generic.ListView):
    model = Artist

class VenueListView(generic.ListView):
    model = Venue

class EventListView(generic.ListView):
    model = Event
    
class ArtistDetailView(generic.DetailView):
    model = Artist
