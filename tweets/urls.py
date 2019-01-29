from django.urls import path,include
from tweets import views
app_name = 'tweets'
urlpatterns = [
	path('',views.soon,name = 'soon'),
	#path('',views.base0,name = 'base0'),             #turn it on after debugging
	path('base/',views.base,name = 'base'),
	path('new_tweet',views.new_tweet,name = 'new_tweet'),
	path('save_tweet',views.save_tweet,name = 'save_tweet'),
	path('ask',views.ask,name = 'ask'),
	path('ask_submit',views.ask_submit,name = 'ask_submit'),


]