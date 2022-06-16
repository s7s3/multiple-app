from django.shortcuts import redirect
from django.urls import path
from django.views import View
from . import views	
urlpatterns = [
    path('', views.root),
    path('register', views.new),
    path('login', views.login),
    path('users', views.users),
    path('users/new', views.new),
]