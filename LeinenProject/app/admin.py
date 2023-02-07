from django.contrib import admin
from .models import *

# Register your models here.

#Con esta clase hacemos que el registro de la galeria se un tabular line (que se pudena aniadir varia lineas al registro)
class AlbumGaleryAdmin(admin.TabularInline):
    model = AlbumGalery


#Con esta clase podemos administrar el modelo dentro del admin, en este caso solo aniadimos que el regstro galery es tabular
class AlbumAdmin(admin.ModelAdmin):
    inlines=[
        AlbumGaleryAdmin
    ]

admin.site.register(CV)
admin.site.register(Software_Skill)
admin.site.register(Album,AlbumAdmin)