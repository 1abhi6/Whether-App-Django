from django.shortcuts import render
import requests


def home(request):
    url = "https://api.openweathermap.org/data/2.5/weather?q={},&appid={}"
    city = "mumbai"
    api_key = "43055cdc7ce9f10e843e86624caa9061"
    resp = requests.get(url.format(city, api_key)).json()

    city_weather = {
        'city': city.capitalize(),
        'temperature': resp['main']['temp'],
        'description': resp['weather'][0]['description'].capitalize(),
        'icon': resp['weather'][0]['icon']
    }

    result = {
        'city_weather': city_weather
    }

    print(city_weather)
    return render(request, 'index.html', result)
