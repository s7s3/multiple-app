from django.shortcuts import redirect
from django.urls import path
from django.views import View
from . import views
urlpatterns = [
    path('', views.root),
    path("surveys", views.index),
    path("surveys/new", views.new),

]