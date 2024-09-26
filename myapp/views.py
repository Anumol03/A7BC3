from django.shortcuts import render,HttpResponse
from .models import *

def index(request):
    services=Services.objects.all()
    return render(request, 'index.html',{"services":services})

def services(request,pk):
    ser=Services.objects.get(id=pk)
    return render(request, 'oasis.html',{"ser":ser})


