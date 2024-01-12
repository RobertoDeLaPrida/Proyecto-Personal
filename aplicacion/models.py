from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name=models.CharField(max_length=30, default='')
    email=models.EmailField()


class Artist(models.Model):
    name=models.CharField(max_length=70)
    born=models.DateField(blank=True,null=True)
    age= models.IntegerField(blank=True,null=True)
    bibiography=models.TextField()
    picture=models.ImageField(upload_to='pictures/',blank=True,null=True)

    def ageCalc(self, *args, **kwargs):
        if self.born:
            age=timezone.now().year-self.born.year

    def __str__ (self):
        return self.name

class Song(models.Model):
    title=models.CharField(max_length=40)
    artist=models.ManyToManyField(Artist)
    lyrics=models.TextField()
    release_date=models.DateField()
    published_on=models.DateTimeField(default=timezone.now)
    cover=models.ImageField(upload_to='covers/',blank=True,null=True)
    SpotifyLink=models.TextField(max_length=150,blank=True,null=True)
    YoutubeLink=models.TextField(max_length=150, blank=True, null=True)
    SoundcloudLink=models.TextField(max_length=150, blank=True, null=True)


    def __str__(self):
        return self.title
    