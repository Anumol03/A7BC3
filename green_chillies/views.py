from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
import json
import csv
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def green_chillies_home(request):
    return render(request, 'green_chillies/index.html')


@csrf_exempt
def create_reservation(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            reservation = Reservation(
                name=data.get('name'),
                phone_number=data.get('phone'),
                email=data.get('email'),
                number_of_persons=data.get('persons'),
                reservation_date=data.get('date'),
                reservation_time=data.get('time')  # Handle the new time field
            )
            reservation.save()
            return JsonResponse({'message': 'Reservation created successfully!'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)


def download_reservations(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="reservations.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Phone Number', 'Email', 'Number of Persons', 'Reservation Date', 'Reservation Time'])

    reservations = Reservation.objects.all().order_by('reservation_date', 'reservation_time')
    for reservation in reservations:
        formatted_date = f"'{reservation.reservation_date.strftime('%d-%m-%Y')}" if reservation.reservation_date else ''
        formatted_time = reservation.reservation_time.strftime('%H:%M') if reservation.reservation_time else ''
        writer.writerow([
            reservation.name,
            reservation.phone_number,
            reservation.email,
            reservation.number_of_persons,
            formatted_date,
            formatted_time
        ])

    return response
