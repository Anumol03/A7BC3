from django.db import models

# Create your models here.

class Reservation(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField()
    number_of_persons = models.PositiveIntegerField(null=True, blank=True)
    reservation_date = models.DateField(null=True, blank=True)
    reservation_time = models.TimeField(null=True, blank=True)  # New time field

    def __str__(self):
        return f"{self.name} - {self.reservation_date} at {self.reservation_time}"
