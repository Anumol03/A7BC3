from django.db import models

# Create your models here.

class Services(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    images = models.ImageField(upload_to='service image',null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return self.name
    