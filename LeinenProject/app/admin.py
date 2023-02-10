from django.contrib import admin
from .models import *

# Register your models here.

#Con esta clase hacemos que el registro de la galeria se un tabular line (que se pudena aniadir varia lineas al registro)
class AlbumGaleryAdmin(admin.StackedInline):
    model = AlbumGalery


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines=[
        AlbumGaleryAdmin
    ]

    class Meta:
        model=Album


@admin.register(AlbumGalery)
class AlbumGaleryAdmin(admin.ModelAdmin):
    pass



#Con esta clase podemos administrar el modelo dentro del admin, en este caso solo aniadimos que el regstro galery es tabular

admin.site.register(CV)
admin.site.register(Software_Skill)
# admin.site.register(Album,AlbumAdmin)