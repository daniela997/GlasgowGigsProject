from django import forms
from django.contrib.auth.models import User
from glasgowgigs.models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bookings', 'favourite_artists', 'favourite_venues')
