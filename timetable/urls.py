from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
app_name = 'timetable'

urlpatterns = [
    
    path('',views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('search/',views.search, name='search'),
]