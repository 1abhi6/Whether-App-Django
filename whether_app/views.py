from django.shortcuts import render
import requests


def home(request):
    url = "https://api.openweathermap.org/data/2.5/weather?q=London,uk&callback=test&appid=43055cdc7ce9f10e843e86624caa9061"
    resp = requests.get(url)
    print(resp.status_code)
    return render(request, 'index.html')
