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


#-------------Image Model------------#
class Image(models.Model):
    image = models.ImageField(upload_to='photos/', null=True)
    image_name = models.CharField(max_length=30)
    image_caption = models.TextField(max_length=100, null=True, blank=True)
    likes = models.IntegerField(null=True, blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True, null=True)
    profile = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User)

    class Meta:
        ordering = ['-date_uploaded']

    def save_image(self):
        '''Method to save an image in the database'''
        self.save()

    def delete_image(self):
        ''' Method to delete an image from the database'''
        self.delete()

    def __str__(self):
        return self.image_name

    @classmethod
    def get_images(cls):
        '''
        Method that gets all image posts from the database
        Returns:
            images : list of image post objects from the database
        '''
        images = Image.objects.all()
        return images
