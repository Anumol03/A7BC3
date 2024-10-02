from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from myapp .models import Email_List
def oasis1(request):

    return render(request, 'oasis1.html')

@csrf_exempt
def save_email_oasis(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            Email_List.objects.create(email=email)
            return JsonResponse({'message': 'Email saved successfully!'}, status=200)
        return JsonResponse({'message': 'Email is required!'}, status=400)
    return JsonResponse({'message': 'Invalid request!'}, status=400)