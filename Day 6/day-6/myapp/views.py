from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
# Create your views here.


def create_user(request):

    if request.method == "POST":

        username = request.POST ["username"]
        password = request.POST ["password"]

        if User.objects.filter(username=username).exists():
            return render(request,'user/user.html',{'error':'User already exists'})
        user = User.objects.create_user(
            username=username,
            password=password
        )
        login(request,user)
        return redirect('show_user')
    return render(request,'user/user.html')

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

#             return redirect('show_user')
#         else:
#             messages.error(request,"Invalid Username or Password")
#             return render(request,'login/login.html')

#     return render(request,'login/login.html')

# def logout_view(request):

#     logout(request)

#     return redirect('login_view')

# class MyLoginView(LoginView):
#     template_name = 'login/login.html'
#     redirect_authenticated_user = True

#     def form_valid(self, form):
#         messages.success(self.request, "Logged in successfully")
#         return super().form_valid(form)

#     def get_success_url(self):
#         return reverse_lazy('show_user')

class MyLoginView(LoginView):
    template_name = 'login/login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        messages.success(self.request, "Logged in successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password")
        return super().form_invalid(form)
        

    def get_success_url(self):
        return reverse_lazy('show_user')
class MyLogoutView(LogoutView):
    next_page = reverse_lazy('login_view')

@login_required
def show_user(request):
    return render(request,"user/user_list.html")

def home(request):

    if request.user.is_authenticated:
        return render(request,'home/home.html')

    return redirect('login_view')