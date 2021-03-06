from django.db import models
from django import forms
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User, Group, Permission
from django.urls import reverse
from django.db.models.signals import post_save
from social_core.backends.facebook import FacebookOAuth2
from social_core.backends.twitter import TwitterOAuth
from embed_video.fields import EmbedVideoField
from datetime import date



class Artist(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(blank=True)
    genre = models.CharField(max_length=128)
    youtube = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    soundcloud = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    info = models.TextField()
    photo = models.ImageField(upload_to='images/artists/', blank=True)
    video = EmbedVideoField(blank=True)

    class Meta:
        permissions = (
            ('perm_add_artist', 'Can add artist'),
        )


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
    latitude = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)
    info = models.TextField(blank=True)
    instagram = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    facebook = models.URLField(blank=True)

    class Meta:
        permissions = (
            ('perm_add_venue', 'Can add venue'),
        )

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
        permissions = (
            ('perm_add_event', 'Can add event'),
        )
        
    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'slug': self.slug})
    @property
    def is_future(self):
        return self.date > date.today()

    @property
    def is_past(self):
        return self.date < date.today()

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    favartists = models.ManyToManyField(Artist, blank=True)
    favvenues = models.ManyToManyField(Venue, blank=True)
    bookings = models.ManyToManyField(Event, blank=True)

    
    
    def __str__(self):
        return self.user.username
        
