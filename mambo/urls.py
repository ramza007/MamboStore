"""
mambo URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^', include('storeapp.urls')),
]
