from django import forms

class CreateUser(forms.Form):
	username = forms.CharField(max_length = 30,label = "User Name")
	email = forms.EmailField(label = "E-Mail")
	password1 = forms.CharField(widget = forms.PasswordInput , label = "password")
	password2 = forms.CharField(widget = forms.PasswordInput,label = "password (again)")