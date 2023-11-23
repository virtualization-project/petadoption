"""
URL configuration for petadoption project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from petadoption.views import home
from petadoption.views import aboutus
from petadoption.views import contact
from petadoption.views import adoption
from petadoption.views import services
from petadoption.views import adminlogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('about-us.html', aboutus),
    path('contacts.html', contact),
    path('blog.html', adoption),
    path('services.html', services),
    path('login.html', adminlogin)
]
