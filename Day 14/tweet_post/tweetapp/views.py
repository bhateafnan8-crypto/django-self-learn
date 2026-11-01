from django.shortcuts import render,redirect,get_object_or_404
from .models import TweetModel
from .forms import TweetForm
# Create your views here.

def home(request):
    return render(request,'home.html')

def tweet_list(request):
    tweets = TweetModel.objects.all()

    return render(request,'tweet_list.html',{'tweets':tweets})

def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request,request.FILES,user = request.user)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            form.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request,'tweet_form.html',{'form':form})

def tweet_edit(request,tweet_id):
    if request.method == "POST":
        form = TweetForm(instance=True,pk=tweet_id)
        if form.is_valid():
            form.save()
            return redirect('tweet_list')

    else:
        form = TweetForm()

    return render(request,'tweet_form.html',{'form':form})

def tweet_delete(request):
    tweet = TweetModel.objects.all()
    if request.method == "POST":
        tweet.delete()
