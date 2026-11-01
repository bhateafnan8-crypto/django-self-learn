from django.shortcuts import render,redirect,get_object_or_404
from .models import TweetModel
from .forms import TweetForm,UserRegistrationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request,'home.html')

#display all tweet posts
def tweet_list(request):
    tweets = TweetModel.objects.all()

    return render(request,'tweet_list.html',{'tweets':tweets})

#create new tweet post
@login_required
def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request,request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            form.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request,'tweet_form.html',{'form':form})

#edit tweet post
@login_required
def tweet_edit(request,tweet_id):
    tweet = get_object_or_404(TweetModel,pk = tweet_id,user = request.user)
    if request.method == "POST":
        form = TweetForm(request.POST,request.FILES,instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            form.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request,'tweet_form.html',{'form':form})

#delete tweet post
@login_required
def tweet_delete(request,tweet_id):
    tweet = get_object_or_404(TweetModel,pk = tweet_id,user = request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect('tweet_list')
    return render(request,'tweet_delete_confirm.html',{'tweet':tweet})


#register new user
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
           user =  form.save(commit=False)
           user.set_password(form.cleaned_data['password1'])
           user.save()
           login(request,user)
        return redirect('tweet_list')
    else:
        form = UserRegistrationForm()

    return render(request,'registeration/register.html',{'form':form})
