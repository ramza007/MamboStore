from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Image, Profile
# , Comment,

#Forms Creation 

class ProfileForm(forms.ModelForm):
    '''
    classs that creates profile update form
    '''
    class Meta:
        model = Profile
        fields = ['profile_photo', 'bio', 'user']