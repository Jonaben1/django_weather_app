import requests
from datetime import datetime
from .secret_key import KEY

def getWeather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={KEY}&units=metric'
    response = requests.get(url).json()
    current_time = datetime.now()
    formatted_time = current_time.strftime('%A, %B %d %Y, %H:%M:%S %p')
    context = {
        'city': city,
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
        'temperature': 'Temperature: ' +  str(response['main']['temp']),
        'country_code': response['sys']['country'],
        'wind': 'Wind: ' + str(response['wind']['speed']) + 'km/h',
        'humidity': 'Humidity: ' + str(response['main']['humidity']) + '%',
        'time': formatted_time
    }
    return context
