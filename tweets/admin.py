from django.contrib import admin

# Register your models here.

from .models import tweets,Ask
admin.site.register(tweets)
admin.site.register(Ask)