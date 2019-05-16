from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('timetable/', include('timetable.urls', namespace='timetable')),
    path('admin/', admin.site.urls),
] 
