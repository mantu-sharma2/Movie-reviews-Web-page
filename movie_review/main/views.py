from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json
from .models import *

# Create your views here.
def home(request):
    allMovies = movie.objects.all()    #queryset
    data = {
        "movies": list(allMovies.values()),
    }
    return JsonResponse(data, safe=False)


# detail page
def details(request, id):
    moviess = movie.objects.get(id=id)
    data = serializers.serialize('json', [moviess,])
    struct = json.loads(data)
    data = {
       "mov1": struct[0],
    }
    return JsonResponse(data, safe=False)

# upvote 
def upvote(request, id):
    m = movie.objects.get(id=id)
    m.Upvote += 1
    m.save()
    data = serializers.serialize('json', [m,])
    struct = json.loads(data)
    data = {
       "mov1": struct[0],
    }
    return JsonResponse(data, safe=False)

def downvote(request,id):
    n=movie.objects.get(id=id)
    n.Downvote-=1
    n.save()
    data=serializers.serialize('json',[n,])
    struct=json.loads(data)
    data={
        'mov1':struct[0]
    }
    return JsonResponse(data,safe=False)