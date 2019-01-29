from django import forms
from .models import tweets,Ask

class TweetsForm(forms.ModelForm):

	class Meta():
		model = tweets
		fields = "__all__"



class AskForm(forms.ModelForm):

	class Meta():
		model = Ask
		fields = "__all__"