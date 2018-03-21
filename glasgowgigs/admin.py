from django.contrib import admin
from glasgowgigs.models import Artist, Venue, Event
from glasgowgigs.models import UserProfile
from embed_video.admin import AdminVideoMixin

# Define the artist class
class ArtistAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ('name', 'likes', 'views', 'genre')
    list_filter = ('likes', 'genre')


# Register the artist class with the associated model
admin.site.register(Artist, ArtistAdmin)

# Define the artist class
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address','likes', 'views')
    


# Register the artist class with the associated model
admin.site.register(Venue, VenueAdmin)

# Define the artist class
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'venue', 'views', 'date', 'bookings')
    list_filter = ('date', 'venue', 'bookings', 'views')
    fieldsets = (
        ('General Information', {
            'fields': ('artist', 'venue', 'date')
        }),
        ('Stats', {
            'fields': ('views', 'bookings')
        }),
    )


# Register the artist class with the associated model
admin.site.register(Event, EventAdmin)

#Register 
admin.site.register(UserProfile)



