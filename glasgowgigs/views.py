from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Artist, Venue, Event
from django.views import generic
from glasgowgigs.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse

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

class VenueDetailView(generic.DetailView):
    model = Venue

class EventDetailView(generic.DetailView):
    model = Event

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)
            
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'glasgowgigs/register.html',
                    {'user_form': user_form,
                    'profile_form': profile_form,
                    'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponseRedirect("Your GlasgowGigs account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'glasgowgigs/login.html', {})

