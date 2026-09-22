from django.shortcuts import render,redirect,get_object_or_404
from stdapp.models import Student
from stdapp.forms import StudentForm,CustomRegisterForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


# register view
def register_view(request):

    if request.method == "POST":
        form = CustomRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully. Please login.")
            return redirect("login")
    else:
        form = CustomRegisterForm()
    return render(request, 'students/register.html', {'form': form})


# login view
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
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'students/login.html')
    # return render(request,'students/login.html')


# logout view
def logout_view(request):

    logout(request)
    return redirect("login")

# dashboard view
@login_required
def std_dashboard(request):
    student_count = Student.objects.filter(owner=request.user).count()
    recent_students = Student.objects.filter(owner=request.user)[:5]

    context = {
        'student_count': student_count,
        'recent_students': recent_students,
    }
    return render(request, 'students/dashboard.html', context)

# this is not wrong but i want to dashboard ui also so add above code
# # dashboard view
# @login_required
# def std_dashboard(request):
#     return redirect('studentform')

# studentform view (fixed: owner assignment + login_required)
@login_required
def std_form_create(request):

    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            student = form.save(commit=False)
            student.owner = request.user
            student.save()

            messages.success(request, "Student created successfully")
            return redirect("stdshow")

    else:
        form = StudentForm()

    return render(request, 'students/student_form.html', {'form': form})


# student_list view (fixed: login_required + only owner's students)
@login_required
def std_show(request):
    std_list = Student.objects.filter(owner=request.user)
    return render(request, 'students/student_list.html', {'std_list': std_list})


# edit / update view
@login_required
def std_update(request, pk):
    student = get_object_or_404(Student, pk=pk, owner=request.user)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully")
            return redirect("stdshow")
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/student_form.html', {'form': form, 'edit': True})


# delete view
@login_required
def std_delete(request, pk):
    student = get_object_or_404(Student, pk=pk, owner=request.user)

    if request.method == "POST":
        student.delete()
        messages.success(request, "Student deleted successfully")
        return redirect("stdshow")

    return render(request, 'students/student_confirm_delete.html', {'student': student})




# some bugs are there 
    # # login view
    # def login_view(request):

    #     if request.method == "POST":

    #         username = request.POST ["username"] 
    #         password = request.POST ["password"]

    #         user = authenticate(
    #             request,
    #             username = username,
    #             password = password
    #         )

    #         if user is not None:
    #             login(request,user)
    #             return redirect('dashboard')
    #     return render(request,'students/login.html')


    # # logout view
    # def logout_view(request):

    #     logout(request)
    #     return redirect("login")


    # # dashboard view + login required
    # @login_required
    # def std_dashboard(request):
    #     return redirect('studentform')


    # # studentform view
    # def std_form_create(request):

    #     if request.method == "POST":

    #         form = StudentForm(request.POST)

    #         if form.is_valid():
    #             form.save()

    #             messages.success(
    #                 request,
    #                 "Student created succesfully"
    #             )

    #             return redirect("stdshow")

    #     else:
    #         form = StudentForm()

    #     return render(request,'students/student_form.html',{'form':form})


    # # student_list - view
    # def std_show(request):

    #     std_list = Student.objects.all()

    #     return render(request,'students/student_list.html',{'std_list':std_list})

