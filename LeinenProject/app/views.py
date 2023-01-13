from django.shortcuts import render, redirect,HttpResponse
# Create your views here.

def home_handler(request):
    return render(request,'layout.html')
