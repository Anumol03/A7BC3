from django.shortcuts import render

# Create your views here.


def fantastic_home(request):
    return render(request,'fantastic/fantastic_home.html')