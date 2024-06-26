"""expertassist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from intmeta.intmetapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('p/intmeta/', views.index, name='index'),
    path('p/intmeta/results', views.results, name='results'),
    path('p/intmeta/kraken', views.kraken, name='kraken'),
    path('p/intmeta/clark', views.clark, name='clark'),
    path('p/intmeta/metamaps', views.metamaps, name='metamaps'),
    path('p/intmeta/about', views.about, name='about'),
    path('p/intmeta/dc', views.dc, name='dc'),
    path('p/intmeta/krona', views.krona, name='krona')
]