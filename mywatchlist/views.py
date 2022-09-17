from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from mywatchlist.models import FilmWatchlist

# Create your views here.
def show_watchlist(request):
    data_film_watchlist = FilmWatchlist.objects.all()
    context = {
        'list_film': data_film_watchlist,
        'nama': 'Ipang'
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