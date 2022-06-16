from multiprocessing import context
import re
from django import http
from django.shortcuts import redirect, render, HttpResponse
from django.http import JsonResponse

def root(request):
    return redirect("/surveys")

def index(request):
    return HttpResponse("placeholder to display all the surveys created")
    
def new(request):
    return HttpResponse("placeholder for users to add a new survey")