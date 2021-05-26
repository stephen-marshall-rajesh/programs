import json
import urllib.request
from pprint import pprint

def get_local_weather():

    weather_base_url = 'http://forecast.weather.gov/MapClick.php?FcstType=json&'

    places = {
        'Austin' : ['30.3074624', '-98.0335911']
    }

    for place in places:

        latitude, logitude = places [place] [0], places [place] [1]
        weather_url = weather_base_url + "lat=" + latitude +"&lon" + logitude

        #show the url we use to get the weather daya
    print("weather_url")
    #print("Getting the current weather for", place, "at, weather_url, ":")

    page_response = urllib.request.urlopen(weather_url).read()