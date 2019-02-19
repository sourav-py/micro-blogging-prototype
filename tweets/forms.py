from django import forms
from .models import tweets

class TweetsForm(forms.ModelForm):

	class Meta():
		model = tweets
		fields = ('body',)