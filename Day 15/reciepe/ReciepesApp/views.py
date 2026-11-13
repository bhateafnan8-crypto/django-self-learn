from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import RecipesModel
# Create your views here.

def home(request):
    return render(request,'home.html')

def reciepe_list(request):
    queryset = RecipesModel.objects.all()
    return render(request,'reciepe_list.html',{'queryset':queryset})

def create_reciepe(request):
    if request.method == "POST":
        data = request.POST
        reciepe_name = data.get('reciepe_name')
        reciepe_description = data.get('reciepe_description')
        reciepe_image = request.FILES.get('reciepe_image')

        RecipesModel.objects.create(
            reciepe_name = reciepe_name,
            reciepe_description = reciepe_description,
            reciepe_image = reciepe_image,
        )
        return redirect('reciepe_list')
    
    return render(request,'reciepe_form.html')

def edit_reciepe(request,id):
    queryset = get_object_or_404(RecipesModel,id = id)

    if request.method == "POST":
        data = request.POST
        reciepe_name = data.get('reciepe_name')
        reciepe_description = data.get('reciepe_description')
        reciepe_image = request.FILES.get('reciepe_image')

        queryset.reciepe_name = reciepe_name
        queryset.reciepe_description = reciepe_description

        if reciepe_image:
            queryset.reciepe_image = reciepe_image

        queryset.save()
        return redirect('reciepe_list')

    return render(request,'reciepe_editform.html')

def delete_reciepe(request,id):
    queryset = get_object_or_404(RecipesModel,id = id)

    if queryset:
        queryset.delete()
        return redirect('reciepe_list')

    return render(request,'reciepe_delete.html')