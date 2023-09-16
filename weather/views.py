from django.shortcuts import render
import requests

# Create your views here.


def find_weather(city):
    API_KEY = "XXXXXXXXXXXXXXXXXXX"
    base_url = (
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    )
    return requests.get(base_url).json()


def search(request):
    weather = {}
    if request.POST:
        city = request.POST.get("main_Input").lower()
        data_set = find_weather(city)
        try:
            weather = dict()
            weather["name"] = data_set["name"]
            weather["country"] = data_set["sys"]["country"]
            weather["main"] = data_set["weather"][0]["main"]
            weather["description"] = data_set["weather"][0]["main"]
            icon_id = data_set["weather"][0]["icon"]
            weather["temp"] = round(data_set["main"]["temp"] - 273.15)
            weather["icon"] = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
            weather["pre"] = data_set["main"]["pressure"]
            weather["hum"] = data_set["main"]["humidity"]
            weather["wind"] = data_set["wind"]["speed"]
        except KeyError:
            print("City not found...")
    return render(request, "home.html", {"weather": weather})
