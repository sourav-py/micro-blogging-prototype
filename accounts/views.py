from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from .forms import CreateUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.


def new_user(request):
	form = CreateUser

	return render(request,'new_user.html',{'form':form})


def create_user(request):
	if request.method == 'POST':
		form = CreateUser(request.POST)
		if form.is_valid():
			username,email,password = form.cleaned_data['username'],form.cleaned_data['email'],form.cleaned_data['password1']
			fresh_user = User.objects.create_user(username,email,password)
			fresh_user.save()
			return HttpResponseRedirect('/')

		else:
			form = CreateUser
			return render(request,'new_user.html',{'form':form})

def profile(request):
	return render(request,'profile.html')

def change_password(request):

	form = PasswordChangeForm(request.user)
	return render(request,'change_password.html',{'form':form})

def change_password_request(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.POST)
		if form.is_valid():
			return HttpResponse('.........')