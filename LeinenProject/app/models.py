from django.db import models

# Create your models here.

class CV(models.Model):
    title=models.CharField(max_length=150,verbose_name="Titulo/trabajo")
    subtitle=models.CharField(max_length=150,verbose_name="Lugar")
    description=models.TextField(verbose_name="Descripcion")
    start_date=models.DateField(verbose_name="Inicio")
    finish_date=models.DateField(verbose_name="Finalizacion")
    public=models.BooleanField(verbose_name="Activo")
    education=models.BooleanField(verbose_name="Titulo_educativo",default='False')


    class Meta():
        verbose_name="Experiencia y estudio"
        verbose_name_plural="Experiencia y estudio"


class Software_Skill(models.Model):
    title=models.CharField(max_length=150)
    public=models.BooleanField(verbose_name="Activo")


class Album(models.Model):
    title=models.CharField(max_length=150,verbose_name="Titulo")
    type=models.CharField(max_length=150,verbose_name="Tipo")
    date=models.DateField(verbose_name="Fecha")
    description=models.CharField(max_length=1500,verbose_name="Descrpción")
    front=models.ImageField(default='null',verbose_name='Portada',upload_to='media')


class AlbumGalery(models.Model):
    image=models.ImageField(upload_to='media')
    
    #poder llamar a las imagenes de un album se le anyade un related_name para poder acceder desde el template referenciando al model "padre"
    title=models.ForeignKey(Album,on_delete=models.CASCADE,related_name="galery")


    



        
