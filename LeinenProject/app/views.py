from django.shortcuts import render, redirect,HttpResponse
# Create your views here.

def home_handler(request):
    return render(request,'home.html')

def about_handler(request):
    return render(request,'about.html')