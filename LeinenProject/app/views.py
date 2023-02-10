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

#
def cv_handler(request):

    education=CV.objects.filter(public=True,education=True)
    works=CV.objects.filter(public=True,education=False)

    skills=Software_Skill.objects.filter(public=True)
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


def portfolio_handler(request):

    albums=Album.objects.all()
    print(albums)

    return render(request,'portfolio.html', {
        'albums':albums
    })


def album_handler(request,id):
    
    album=Album.objects.get(id=id)
    #Para sacar la lista de imagenes, hacer que saque las que tengan el mismo title_id
    #despues en el tamplate con hacer un for y mostrarlaas con picture.image.url
    gallery=AlbumGalery.objects.filter(title_id=id)

    return render(request,"album_gallery.html",{
        'album':album, 
        'gallery':gallery
    })
