from multiprocessing import context
import re
from django import http
from django.shortcuts import redirect, render, HttpResponse
from django.http import JsonResponse

def root(request):
    return redirect("/blogs")
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog") 
def create(request):
    return redirect('/')


def show(request,number):
   number = f"placeholder to display blog {number}"
   return HttpResponse(number)

def edit(request,number):
   number = f"placeholder to edit blog {number}"
   return HttpResponse(number)

def delete(request,number):
   number= "Delete article Number : %s" %number
   return redirect("/blogs")

def json(request):
    return JsonResponse({
        'title':'my first blog',
       ' content_key':'ljgsadoiuqwefgo  qiuewgd pqiwugdbiuwqgdvb '

    })