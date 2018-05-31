from django.db import models
from django.contrib.auth.models import User
import datetime as dt

# Create your models here.
#------------Profile Model-------------#
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profiles/', null=True)
    bio = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        '''
        Display for profiles in profile table
        '''
        return self.user.username

    @classmethod
    def get_profiles(cls):
        '''
        Fucntion that gets all the profiles in the app
        Return
        '''
        profiles = Profile.objects.all()

        return profiles

    @classmethod
    def search_by_grammer(cls, search_term):
        query = cls.objects.filter(bio__icontains=search_term)
        return query