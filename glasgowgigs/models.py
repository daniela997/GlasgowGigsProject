from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse


class Artist(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(blank=True)
    genre = models.CharField(max_length=128)
    youtube = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    soundcloud = models.URLField(blank=True)
    info = models.TextField()
    photo = models.ImageField(upload_to='images/artists/', blank=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Artist, self).save(*args, **kwargs)

    def __str__(self): # For Python 2, use __unicode__ too
        return self.name

    def get_absolute_url(self):
        return reverse('artist-detail', kwargs={'slug': self.slug})


class Venue(models.Model):
    name = models.CharField(max_length=128, unique=True)
    address = models.CharField(max_length=128) 
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(blank=True)
    photo = models.ImageField(upload_to='images/venues/', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Venue, self).save(*args, **kwargs)

    def __str__(self): # For Python 2, use __unicode__ too
        return self.name

    def get_absolute_url(self):
        return reverse('venue-detail', kwargs={'slug': self.slug})
    
class Event(models.Model):
    venue = models.ForeignKey(Venue)
    artist = models.ForeignKey(Artist)
    date = models.DateField()
    name = models.CharField(max_length=128, blank=True)
    bookings = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    slug = models.SlugField(blank=True)
   
    def __str__(self): # For Python 2, use __unicode__ too
        return self.name
    def save (self, *args, **kwargs):
        if self.venue and self.artist and self.date:
            self.name = self.artist.name+" @ "+self.venue.name+" on "+str(self.date)
        self.slug = slugify(self.name)
        super(Event, self).save(*args, **kwargs)

    class Meta:
        unique_together = ('venue', 'artist', 'date')
        # to make sure that we don't have two instances of an event with of the same artist in the same venue at the same time

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'slug': self.slug})

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    bookings = models.ManyToManyField(Event)
    favourite_artists = models.ManyToManyField(Artist)
    favourite_venues = models.ManyToManyField(Venue)
    
    def __str__(self):
        return self.user.username
