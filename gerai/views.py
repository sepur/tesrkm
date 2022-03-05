from django.shortcuts import render
from django.http import HttpResponse
from .models import TblTes
import requests,json
from urllib import request
import urllib.request as ur

def tampil(request):
    linkk = 'https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json'
    cb = ur.urlopen(linkk)
    data = json.loads(cb.read())
    return render(request,'gerai/tampil.html',{'jasa':data,})

def index(request):
    tes = TblTes.objects.all()
    return render(request,'gerai/show.html',{'tes':tes})
    #return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.

