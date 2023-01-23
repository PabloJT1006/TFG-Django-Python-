from django.shortcuts import render, redirect,HttpResponse
from .form import FormContacto

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
            



    return render(request,'contacto.html')