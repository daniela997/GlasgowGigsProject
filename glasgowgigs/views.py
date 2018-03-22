from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Artist, Venue, Event
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

class IndexView(generic.ListView):
    # Define the template to be used
    template_name = 'glasgowgigs/index.html'

class ArtistListView(generic.ListView):
    # Define model to be used
    model = Artist
    template_name = 'glasgowgigs/artist_list.html'

class VenueListView(generic.ListView):
    model = Venue
    template_name = 'glasgowgigs/venue_list.html'


class EventListView(generic.ListView):
    model = Event
    template_name = 'glasgowgigs/event_list.html'

    
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
    if request.method == 'GET':
		
        venuename = request.GET['venue']
    likes = 0
    if venuename:
        venue = Venue.objects.get(name=venuename)
        if venue:
            likes = venue.likes + 1
            venue.likes = likes
            venue.save()
    return HttpResponse(likes)

