from django.shortcuts import render
import requests


def home(request):
    result = {}
    city = ""
    query = ""
    if request.method == 'POST':
        try:

            url = "https://api.openweathermap.org/data/2.5/weather?q={},&appid={}"
            query = request.POST.get('queryBox')
            city = query.lower()
            api_key = "43055cdc7ce9f10e843e86624caa9061"
            resp = requests.get(url.format(city, api_key)).json()

            city_weather = {
                'city': city.capitalize(),
                'temperature': round(resp['main']['temp']-273.15, 2),
                'description': resp['weather'][0]['description'].capitalize(),
                'icon': resp['weather'][0]['icon'],
                'status':True
            }

            result = {
                'city_weather': city_weather,
            }
        except:
            pass

    return render(request, 'index.html', result)
