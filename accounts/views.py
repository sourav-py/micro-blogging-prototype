from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from .forms import CreateUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash , authenticate

# Create your views here.




def create_user(request):
	if request.method == 'POST':
		form = CreateUser(request.POST)
		if form.is_valid():
			username,email,password = form.cleaned_data['username'],form.cleaned_data['email'],form.cleaned_data['password1']
			fresh_user = User.objects.create_user(username,email,password)
			fresh_user = authenticate(username=username,password=password)
			fresh_user.save()
			return HttpResponseRedirect('/')

		else:
			return HttpResponse('invalid form')

	else:
		form = CreateUser
		return render(request,'new_user.html',{'form':form})

def profile(request):
	return render(request,'profile.html')



def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST,user = request.user)
		if form.is_valid():
			
			
			form.save()
			update_session_auth_hash(request,form.user)
			return HttpResponseRedirect('/accounts/profile')



		else:
			return HttpResponse('invalid submission')

	else:
		form = PasswordChangeForm(user = request.user)
		return render(request,'change_password.html',{'form':form})







