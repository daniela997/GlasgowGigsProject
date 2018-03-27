from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from glasgowgigs.models import Artist, Venue, Event, User, UserProfile
from django.views import generic
from glasgowgigs.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from social_django.models import UserSocialAuth
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.views.generic.list import ListView


def index(request):
    # stats
    num_artists=Artist.objects.all().count()
    num_venues=Venue.objects.all().count()
    num_events=Event.objects.all().count()

    artist_top5 = Artist.objects.order_by('-likes')[:5]
    venue_top5 = Venue.objects.order_by('-likes')[:5]
    
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'glasgowgigs/index.html',
        context={'num_artists':num_artists,'num_venues':num_venues,'num_events':num_events,'top_artists':artist_top5, 'top_venues':venue_top5},
    )

    

def about(request):
    context_dict = {}
    return render(request, 'glasgowgigs/about.html', context=context_dict)

class IndexView(generic.ListView):
    # Define the template to be used
    template_name = 'glasgowgigs/index.html'

class ArtistListView(generic.ListView):
    # Define model to be used
    model = Artist
    template_name = 'glasgowgigs/artist_list.html'
    ordering = ['-likes']

class VenueListView(generic.ListView):
    model = Venue
    template_name = 'glasgowgigs/venue_list.html'
    ordering = ['-likes']

class EventListView(generic.ListView):
    model = Event
    template_name = 'glasgowgigs/event_list.html'
    ordering = ['date']


class ArtistDetailView(generic.DetailView):
    model = Artist
    def get_context_data(self, **kwargs):
        context = super(ArtistDetailView, self).get_context_data(**kwargs)
        context['events'] = Event.objects.filter(artist=self.object)
        return context

class VenueDetailView(generic.DetailView):
    model = Venue
    def get_context_data(self, **kwargs):
        context = super(VenueDetailView, self).get_context_data(**kwargs)
        context['events'] = Event.objects.filter(venue=self.object)
        return context

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


@login_required
def settings(request):
    user = request.user

    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'registration/settings.html', {
        'twitter_login': twitter_login,
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })

@login_required
def profile(request):
    user = request.user
    userprofile = UserProfile.objects.get_or_create(user=user)[0]

    bookings = userprofile.bookings.all().order_by('date')
    favourite_artists = userprofile.favartists.all().order_by('-likes') 
    favourite_venues = userprofile.favvenues.all().order_by('-likes') 

         
    return render(request, 'registration/profile.html', context={'bookings':bookings, 'favartists':favourite_artists, 'favvenues':favourite_venues})

@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'registration/password.html', {'form': form})

@login_required
def restricted(request):
    return HttpResponse("Since you are logged in, you can see this text!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def like_venue(request):
    user = request.user
    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    venue_id = None
    if request.method == 'GET':
        venue_id = request.GET['venue_id']
    likes = 0
    if venue_id:
        venue = Venue.objects.get(id=venue_id)
        if venue:
            likes = venue.likes + 1
            venue.likes = likes
            venue.save()
            userprofile.favvenues.add(Venue.objects.get(id=venue_id))

    return HttpResponse(likes)

@login_required
def like_artist(request):
    user = request.user
    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    artist_id = None
    if request.method == 'GET':
        artist_id = request.GET.get('artist_id')
    likes = 0
    if artist_id:
        artist = Artist.objects.get(id=artist_id)
        if artist:
            likes = artist.likes + 1
            artist.likes = likes
            artist.save()
            userprofile.favartists.add(Artist.objects.get(id=artist_id))
    return HttpResponse(likes)

    
@login_required
def book_event(request):
    user = request.user
    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    event_id = None
    if request.method == 'GET':
        event_id = request.GET.get('event_id')
    if event_id:
        event = Event.objects.get(id=event_id)
        if event in userprofile.bookings.all():
            userprofile.bookings.remove(Event.objects.get(id=event_id))
        else:
            userprofile.bookings.add(Event.objects.get(id=event_id))
    return HttpResponse()



    

