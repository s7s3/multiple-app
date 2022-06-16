from multiprocessing import context
import re
from django import http
from django.shortcuts import redirect, render, HttpResponse
from django.http import JsonResponse

def root(request):
    return redirect("/users")

def new(request):
    return HttpResponse("placeholder for users to create a new user record")

def login(request):
    return HttpResponse("placeholder for users to log in")

def users(request):
    return HttpResponse("placeholder to later display all the list of users") 

   