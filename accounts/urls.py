from django.urls import path,include
from accounts import views

urlpatterns = [

	path('new_user',views.new_user,name = 'new_user'),
	path('create_user',views.create_user,name= 'create_user'),
	path('change_password',views.change_password,name = 'change_password'),
    path('profile',views.profile,name = 'profile'),
    path('change_password_request',views.change_password_request,name = 'change_password_request'),
]