from django.shortcuts import render


# Create your views here.

def green_chillies_home(request):
    return render(request, 'green_chillies/index.html')
