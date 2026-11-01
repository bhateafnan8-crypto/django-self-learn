from django import forms
from .models import TweetModel
from django.contrib.auth.forms import UserCreationForm

class TweetForm(forms.ModelForm):

    class Meta:

        model = TweetModel
        fields = ['text','photo']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:

        model = TweetModel
        fields = ('username','email','password1','password2')
        