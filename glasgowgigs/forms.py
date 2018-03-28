from django import forms
from django.contrib.auth.models import User, Group
from glasgowgigs.models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=False)
    class Meta:
        model = UserProfile
        fields = ('bookings', 'favartists', 'favvenues', 'group')

# did not have enough time to implement this, will do it in the future!

# class ArtistForm(forms.ModelForm):

