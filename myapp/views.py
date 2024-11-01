from django.shortcuts import render, HttpResponse,redirect
from .models import *
from django.http import JsonResponse
import csv
from django.http import HttpResponse
from .models import Email_List
from django.contrib.auth.decorators import user_passes_test
from datetime import datetime
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
def index(request):
    service = Services.objects.all()
    return render(request, 'new_index.html', {"services": service})


def submit_contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Create the object in the database
        Email_List.objects.create(name=name, email=email, message=message)

        # Return a JSON response
        return JsonResponse({'status': 'success', 'message': 'Feedback posted successfully, we will get back to you.'})

    # If the request method is not POST, return an error (this case is optional)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


def services(request, pk):
    ser = Services.objects.get(id=pk)
    return render(request, 'oasis.html', {"ser": ser})


# @user_passes_test(lambda u: u.is_superuser)
def download_email_list_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="email_list_{}.csv"'.format(
        datetime.now().strftime("%Y%m%d"))

    writer = csv.writer(response)
    writer.writerow(['Name', 'Email', 'Date'])

    email_list = Email_List.objects.all().values_list('name', 'email', 'date')
    for email in email_list:
        writer.writerow(email)

    return response


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('index')  # Redirect to the home page or another page
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    return render(request, 'login.html')


def user_logout(request):
    logout(request)  # This will log the user out
    messages.success(request, 'You have been logged out.')
    return redirect('index')  # Redirect to the login page or another page
