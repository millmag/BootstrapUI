from django.shortcuts import render
from .models import Schedule
from .utils import locations, timetable

# Create your views here.


def home(request):

    
    return render(request, 'home.html', {'times' :None})


def search(request):
    if not request.GET.get('location', False):
         return render(request, 'home.html', {'times' :None})
    else:
        location = request.GET['location']
        location = str(location.upper())

        times = Schedule.objects.filter(area__area=location)

        if not times:
            info = None
            return render(request, 'home.html', {'times':info})
        else:
            print(location)
            return render(request, 'home.html', {'times' : times, 'location':location})