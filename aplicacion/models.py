from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from wsgiref.validate import validator
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.

class User(AbstractUser):
    photo = models.ImageField(upload_to='profile_pictures/', blank=True,null=True)
    friends = models.ManyToManyField('self', symmetrical=True)

    def __str__ (self):
        return self.username


class Artist(models.Model):
    name=models.CharField(max_length=70)
    born=models.DateField(blank=True,null=True)
    biography=models.TextField()
    picture=models.ImageField(upload_to='pictures/',blank=True,null=True)
    group = models.BooleanField(default=False)


    def __str__ (self):
        return self.name

class Song(models.Model):
    title=models.CharField(max_length=40)
    artist=models.ManyToManyField(Artist)
    lyrics=models.TextField()
    release_date=models.DateField()
    cover=models.ImageField(upload_to='covers/',blank=True,null=True)
    SpotifyLink=models.TextField(max_length=150,blank=True,null=True)
    YoutubeLink=models.TextField(max_length=150, blank=True, null=True)
    SoundcloudLink=models.TextField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.title
    
class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, default='')
    opinion = models.TextField()
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__ (self):
        return self.title
    
