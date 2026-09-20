from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    age = forms.IntegerField()
    is_pass = forms.BooleanField()

class UserForm(forms.Form):
    name = forms.CharField(max_length=50)
    is_paid = forms.ChoiceField(choices=[('paid','Paid'),('unpaid','Unpaid')])