from django.contrib import admin
from glasgowgigs.models import Artist, Venue, Event

# Define the artist class
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'likes', 'views', 'genre')



# Register the artist class with the associated model
admin.site.register(Artist, ArtistAdmin)

# Define the artist class
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address','likes', 'views')
    


# Register the artist class with the associated model
admin.site.register(Venue, VenueAdmin)

# Define the artist class
class EventAdmin(admin.ModelAdmin):
    list_display = ('artist', 'venue', 'views', 'date', 'bookings')
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


