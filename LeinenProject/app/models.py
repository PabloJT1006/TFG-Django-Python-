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

    def __str__(self) -> str :
        return f"{self.title}"



class Software_Skill(models.Model):
    title=models.CharField(max_length=150)
    public=models.BooleanField(verbose_name="Activo")

    def __str__(self) -> str :
        return f"{self.title}"
    


class Album(models.Model):
    title=models.CharField(max_length=150,verbose_name="Titulo")
    type=models.CharField(max_length=150,verbose_name="Tipo")
    date=models.DateField(verbose_name="Fecha")
    description=models.CharField(max_length=1500,verbose_name="Descrpción")
    front=models.ImageField(default='null',verbose_name='Portada',upload_to='media/')
    slug = models.CharField(unique=True,max_length=50,verbose_name="Url",default='null')


    def __str__(self) -> str :
        return f"{self.title}"


class AlbumGalery(models.Model):
    image=models.ImageField(upload_to='media/')
    
    #poder llamar a las imagenes de un album se le anyade un related_name para poder acceder desde el template referenciando al model "padre"
    title=models.ForeignKey(Album,on_delete=models.CASCADE,related_name="galery")

    class Meta():
        verbose_name_plural="Album Gallery"



    

class Contact(models.Model):
    name=models.CharField(max_length=150,verbose_name="Nombre cliente")
    mail=models.CharField(max_length=150,verbose_name="Mail")
    project=models.CharField(max_length=150,verbose_name="Proyecto")
    message=models.TextField(verbose_name="Mensaje")
    read=models.BooleanField(default=False,verbose_name="Leido?")
    

    def __str__(self) -> str:
        
        if self.read:
            leido="Leido"
        else:
            leido="No liedo"
        
        return f"{self.mail}, {leido}"
    
    
            



class Home(models.Model):
    banner_img = models.ImageField(default="null", upload_to="media/", verbose_name="Imagen Banner")
    banner_title = models.CharField(max_length=50, verbose_name="Titulo banner")
    banner_subtitle = models.CharField(max_length=50, verbose_name="Subtitulo banner")
    presentation_text = models.TextField(max_length=500, verbose_name="Texto Presentacion")
    active=models.BooleanField(verbose_name="Publico?",default=False)




    class Meta():
        verbose_name_plural="Home"



   
   
class Videos(models.Model):   
    iframes = models.CharField(max_length=999,verbose_name="Iframe del video")
    title = models.CharField(max_length=50,verbose_name="Titulo del video")
    public=models.BooleanField(default=False,verbose_name="Publicado?")

    def __str__(self) -> str :
        
        if self.public:
            publicado="(Publicado)"
        else:
            publicado=("(No Publicado)")
        
        return f"{self.title}, {publicado}"
        

    class Meta():
        verbose_name="Video"
        verbose_name_plural="Videos"

    

class About(models.Model):
    title=models.CharField(max_length=150,verbose_name="Titulo")
    subtitle=models.CharField(max_length=150,verbose_name="Subititulo")
    content=models.TextField(max_length=9999,verbose_name="Descripcion")
    img=models.ImageField(verbose_name="Imagen",default="null",upload_to="media/" )
    active=models.BooleanField(verbose_name="Publico?",default=False)
    
    class Meta():
        verbose_name_plural="About"



    
        