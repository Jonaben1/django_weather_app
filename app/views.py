from django.shortcuts import render
from .weather import getWeather

# Create your views here.

def index(request):
     try:
         if request.method == 'POST':
             city = request.POST['city']
             context = getWeather(city)
             return render(request, 'home.html', context)
         else:
             city_weather = {}
             context = {'city_weather': city_weather}
             return render(request, 'home.html', context)
     except:
        return render(request, 'error.html')
