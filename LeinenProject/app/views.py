from django.shortcuts import render, redirect,HttpResponse
from .form import FormContacto
from django.contrib import messages
from app.models import *


# Create your views here.

def home_handler(request):
    return render(request,'home.html')

def about_handler(request):
    return render(request,'about.html')


def contacto_handler(request):

    if request.method == 'POST':
        form=FormContacto(request.POST)

        if form.is_valid():
            #limpiar los datos y sacar lo introducido
            data_form=form.cleaned_data

            messages.success(request,f"Mensaje mandado con exito")

               
    else:
            form=FormContacto()    



    return render(request,'contacto.html',{
        'form':form
    })


def cv_handler(request):

    education=CV.objects.filter(public=True,education=True)
    works=CV.objects.filter(public=True,education=False)

    skills=Software_Skills.objects.filter(public=True)
    def order_skills(skills):
        left=[]
        right=[]

        x=len(skills)

        for skill in skills:
            if x%2 ==0:
                left.append(skill)
            else:
                right.append(skill)
            x-=1
        
        skills={'right':right,'left':left}

        return skills

    

    return render(request,'cv.html',{
        'studies':education,
        'works':works,
        'skills':order_skills(skills),
        

    })