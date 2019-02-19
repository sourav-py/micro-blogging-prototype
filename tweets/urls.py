from django.urls import path,include
from tweets import views
app_name = 'tweets'
urlpatterns = [
	#path('',views.base0,name = 'base0'),
	path('',views.base,name = 'base'),
	path('new_tweet',views.new_tweet,name = 'new_tweet'),
	path('save_tweet',views.save_tweet,name = 'save_tweet'),


]