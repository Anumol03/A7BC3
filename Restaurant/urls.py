"""Restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static
from spices.views import *
from Fantastic_frames_app import views as ff
from green_chillies import views as gc
from oasis.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('download-email-list-csv/', download_email_list_csv, name='download_email_list_csv'),
    path('submit-contact/', submit_contact_form, name='submit_contact_form'),
    path('services/<int:pk>/', services, name='service_page'),
    path('spices/', spices, name='spices'),
    path('fantastic/', ff.fantastic_home, name='fantastic-home'),
    path('oasis/', oasis1, name='oasis'),
    path('green-chillies/', gc.green_chillies_home, name='green-chillies'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
