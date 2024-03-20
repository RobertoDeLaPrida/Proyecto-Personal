from django.contrib import admin
from .models import Song,Artist,User,Review
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
    (None, {'fields': ('photo','friends')}),
    )
    #Con esto te saldra al crear un nuevo usuario desde admin los campos
    add_fieldsets = UserAdmin.add_fieldsets + (
    (None, {'fields': ('photo','friends')}),
    )

admin.site.register(Song)
admin.site.register(Artist)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Review)