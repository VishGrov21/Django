from django.urls import path
from basicApp import views

#Template Tagging
app_name='basicApp'
urlpatterns = [
path('', views.index, name='index'),
path('register', views.register, name='register'),
path('login', views.user_login, name='login'),
path('logout', views.user_logout, name='logout'),
path('special', views.special, name='special'),

]
