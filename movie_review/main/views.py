from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json
from .models import *

# Create your views here.
def home(request):
    allMovies = movie.objects.all()
    # print(allMovies.values())
    data = {
        "movies": list(allMovies.values()),
    }
    return JsonResponse(data, safe=False)
    # return render(request,'main/index.html', context)

# detail page
def details(request, id):
    moviess = movie.objects.get(id=id)
    # print(moviess)
    data = serializers.serialize('json', [moviess,])
    struct = json.loads(data)
    data = {
       "mov1": struct[0],
    }
    return JsonResponse(data, safe=False)
    # return render(request, 'main/details.html', context)

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
