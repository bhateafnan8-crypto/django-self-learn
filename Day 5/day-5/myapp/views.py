from django.shortcuts import render,redirect
from myapp.forms import StudentForm,UserForm,CustomerbillForm,InvoiceForm,FeedbackForm,JobForm
from myapp.models import Job,Invoice,Feedback
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
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


# ModelForm.. editing/Updating an existing object

def job_create(request):

    jobs, _ = Job.objects.get_or_create(id=1,defaults={'name': '', 'type': '', 'cgpa': 0, 'experience': ''}) # in before i have wrote this inside the if block , and access it an else block means it should in globally scope but i had do as block scop. not exist or.. exact error "cannot access local variable 'jobs' where it is not associated with a value",

    if request.method == "POST":

        # form = JobForm(request.POST) # this one will be overwrite from below so it not required because i want to update the form in an existing object
        # jobs = Job.objects.get(id=1) # this one will be give error because there is no data exist in db so want to add default values and use getorcreate for if not get so first create and update

        
        form = JobForm(
            request.POST,
            instance=jobs
        )


        if form.is_valid():
            form.save()

    else:
        form = JobForm(instance=jobs)

        # form = JobForm() this one is not wrong but here also want for update . means it will create without updating but want to update so use instance=jobs here also..



    return render(request,'Job/job.html',{'form':form})


# authentication - User

"""user = User.objects.create_user(username='john',email='john@ex.com',password='secrete123') 
User.objects.all()  # issue here these two lines create user multiple times thats why this occur"django.db.utils.IntegrityError: UNIQUE constraint failed: auth_user.username""

if not User.objects.filter(username='john').exists(): # these two lines right but not required here
    User.objects.create_user(username='john', email='john@ex.com', password='secrete123') """

# login
def login_view(request):

    if request.method == "POST":

        username = request.POST ["username"]
        password = request.POST ["password"] 

        user = authenticate(
            request,
            username = username,
            password = password
        )

        if user is not None:
            login(request,user)
  


    return render(request,'login/login.html')

# logout
def logout_view(request):
    logout(request)
    return redirect("login_view") # here add the name='login_view' this attribute value which one is add at urls.py file.. but i was add login means the file name of html..

# for login-requires 
@login_required
def dashboard(request):
    return redirect(request,'dashboard/dashboard.html')