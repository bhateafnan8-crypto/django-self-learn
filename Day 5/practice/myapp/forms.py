from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from myapp.models import Student

class UserForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    age =  forms.IntegerField()

    def clean_age(self):
        age = self.cleaned_data["age"]

        if age >= 18:
            raise forms.ValidationError(
                "above 18 not valid"
            )

        return age

    def __str__(self):
        return self.name

class StudentForm(forms.ModelForm):

    class Meta:

        model = Student
        fields = ['name','email','age','course']