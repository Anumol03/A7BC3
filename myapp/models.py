from django.db import models


# Create your models here.

class Services(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    images = models.ImageField(upload_to='service image', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    icon_image = models.ImageField(upload_to='icons', null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    phone_no = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Email_List(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    message = models.TextField(null=True,blank=True)
    mob = models.CharField(max_length=20, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
