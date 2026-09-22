from django import forms
from django.contrib.auth.forms import UserCreationForm
from stdapp.models import Student
from django.contrib.auth.models import User
class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['name', 'email', 'phone', 'age', 'gender', 'course', 'address']
class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']