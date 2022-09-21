from pickle import TRUE
from django.shortcuts import render
from mywatchlist.models import FilmWatchlist
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_watchlist(request):
    data_film_watchlist = FilmWatchlist.objects.all()
    watched = 0
    unwatched = 0
    pesan = ""
    for i in data_film_watchlist:
        if i.watched == True:
            watched+=1
        else:
            unwatched+=1
    if watched >= unwatched:
        pesan = "Selamat, kamu sudah banyak menonton!"
    else:
        pesan ="Wah, kamu masih sedikit menonton!"
    context = {
        'list_film': data_film_watchlist,
        'nama': 'Ipang',
        'pesan' : pesan
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = FilmWatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = FilmWatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = FilmWatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")