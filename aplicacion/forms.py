from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Review, User

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ["username","first_name","last_name","email","photo"]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title','opinion']