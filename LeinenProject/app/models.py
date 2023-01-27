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


class Software_Skills(models.Model):
    title=models.CharField(max_length=150)
    public=models.BooleanField(verbose_name="Activo")


        
