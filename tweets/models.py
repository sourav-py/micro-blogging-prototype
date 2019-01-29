from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class tweets(models.Model):
	def curr_user():
		for user in User.objects.all():
			if user.is_active:
				return user.get_username
	z = curr_user()
	k = datetime.now
	author = models.CharField(max_length = 50,default=z)
	date_time = models.DateTimeField(default = k)
	body = models.TextField()



	def __str__(self):
		return self.body


class Ask(models.Model):

	name = models.CharField(max_length=100)
	email = models.EmailField()
	question = models.TextField()


	def __str__(self):

		return self.name