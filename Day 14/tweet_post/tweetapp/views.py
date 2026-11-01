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
        form = TweetForm(request,request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            form.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request,'tweet_form.html',{'form':form})

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

def tweet_delete(request,tweet_id):
    tweet = get_object_or_404(TweetModel,pk = tweet_id,user = request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect('tweet_list')
    return render(request,'tweet_delete_confirm.html',{'tweet':tweet})