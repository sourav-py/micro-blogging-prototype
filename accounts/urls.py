from django.urls import path,include
from accounts import views

app_name = 'accounts'
urlpatterns = [
	
	path('create_user',views.create_user,name= 'create_user'),
	path('change_password',views.change_password,name = 'change_password'),
    path('profile',views.profile,name = 'profile'),
    path('change_password',views.change_password,name = 'change_password'),
    
]