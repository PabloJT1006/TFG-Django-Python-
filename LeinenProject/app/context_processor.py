from .models import Album 

def get_album(request):
    albums=Album.objects.values_list("id","slug","front")

    return {
        'albums':albums 
    }