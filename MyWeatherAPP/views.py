from django.shortcuts import render
import json
import urllib.request


# Create your views here.
def home(request):
    return render(request, 'MyWeatherAPP/index.html')


def home(request):
    if request.method == 'POST':
        # Get the city name from the user api = http://api.openweathermap.org/data/2.5/weather
        city = request.POST.get('city', 'True')

        # retreive the information using api
        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=imperial&appid=b4a30a5a572f027b8d964939e477b452').read()

        # convert json data file into python dictionary
        list_of_data = json.loads(source)

        # create dictionary and convert value in string
        context = {
            'city': city,
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                          + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }
    else:
        context = {}

        # send dictionary to the index.html
    return render(request, 'MyWeatherAPP/index.html', context)
