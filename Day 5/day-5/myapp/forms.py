from django import forms
from myapp.models import Invoice,Feedback,Job,Student

# simple way
class StudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    age = forms.IntegerField()
    is_pass = forms.BooleanField()

#  (method = post) + validation 
class UserForm(forms.Form):
    name = forms.CharField(max_length=50)
    is_paid = forms.ChoiceField(choices=[('paid','Paid'),('unpaid','Unpaid')])


#  custom validation

class CustomerbillForm(forms.Form):
    name = forms.CharField(max_length=50)
    phone = forms.IntegerField()
    is_offer = forms.ChoiceField(choices=[('active','Active'),('inactive','Inactive')])

    def clean_phone(self):

        phone = self.cleaned_data["phone"]
        # phone = self.cleaned_data("phone") # here is also wrong () this pass a dict ,want to pass list so use []


        if len(str(phone)) != 10:
            raise forms.ValidationError(
                "Phone number should be 10 digit only"
            )
# i want to check here len/digit but i do check direct value..
        # if phone != 10:  
        #     raise forms.ValidationError(
        #         "Phone number should be 10 digit only"
        #     )

        return phone

# modal-form

class InvoiceForm(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = ["name","inv_id","amount"]


# model-form . object creation

class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields =["name","email","subject","message","rating"]


# ModelForm.. editing/Updating an existing object

class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ['name','type','cgpa','experience']

# mediaForm

class StudentForm(forms.Form):

    class Meta:
        model = Student
        fields = ['name','photo']