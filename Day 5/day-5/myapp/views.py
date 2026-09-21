from django.shortcuts import render
from myapp.forms import StudentForm,UserForm,CustomerbillForm,InvoiceForm,FeedbackForm
# Create your views here.

# simple forms.Form
def student_create(request):
    form = StudentForm()
    return render(request,'student/studentform.html',{'form':form})

# (method= Post) + validation
def user_create(request):

    if request.method == "POST":
        form = UserForm(request.POST) # create with post method

        if form.is_valid():
            print(form.cleaned_data) # return data if valid

    else:
        form = UserForm() # create form if not valid

    return render(request, "user/user.html", {"form": form})

# custom validation
def customer_bill_create(request):

    if request.method == "POST":
        form = CustomerbillForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)

    else:
        form = CustomerbillForm()

    return render(request,'customerbill/customer_bill.html',{'form':form})

# simple ModelForm
def invoice_create(request):

    if request.method == "POST":
        form = InvoiceForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)

    else:
        form = InvoiceForm()

    return render(request,'Invoice/invoice.html',{'form':form})

# object creation . ModelForm
def feedback_create(request):

    if request.method == "POST":

        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save() # create database record
    else:
        form = FeedbackForm()

    return render(request,'Feedback/feedback.html',{'form':form})
    