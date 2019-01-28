from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from .forms import TweetsForm
from .models import tweets

# Create your views here.

def soon(request):
	return render(request,'soon.html')

def base0(request):
	return render(request,'base0.html')

def base(request):
	models = tweets.objects.all()
	
	return render(request,'base.html',{'models':models})

def new_tweet(request):
	form = TweetsForm
	return render(request,'new_tweet.html',{'form': form})


def save_tweet(request):
	if request.method == 'POST':
		form = TweetsForm(request.POST)
		if form.is_valid():
			
			form.save()
			return HttpResponseRedirect('/base/')