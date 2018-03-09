from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __str__(self): # For Python 2, use __unicode__ too
        return self.name


class Venue(models.Model):
    name = models.CharField(max_length=128, unique=True)
    address = models.CharField(max_length=128, unique=True) 
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __str__(self): # For Python 2, use __unicode__ too
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=128)
    venue = models.ForeignKey(Venue)
    artist = models.ForeignKey(Artist)
    date = models.DateField()
    bookings = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __str__(self): # For Python 2, use __unicode__ too
        return self.name
    def save (self, *args, **kwargs):
        if self.venue and self.artist:
            self.name = self.artist.name+" @ "+self.venue.name
        super(Event, self).save(*args, **kwargs)

