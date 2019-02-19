from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from .forms import TweetsForm
from .models import tweets
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.



#def base0(request):
	#return render(request,'base0.html')

@login_required(login_url = '/auth_urls/login/')
def base(request):
	models = tweets.objects.all()
	
	return render(request,'base.html',{'models':models})
@login_required
def new_tweet(request):
	form = TweetsForm()
	return render(request,'new_tweet.html',{'form': form})


def save_tweet(request):
	if request.method == 'POST':
		form = TweetsForm(request.POST,request.user)
		if form.is_valid():
			stock = form.save(commit = False)
			stock.author = request.user
			stock.save()
			return HttpResponseRedirect('/')
		else: 
			return HttpResponse('invalid form submission')