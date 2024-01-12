from django.contrib import admin
from .models import Song,Artist,User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(Song)
admin.site.register(Artist)
admin.site.register(User, UserAdmin)