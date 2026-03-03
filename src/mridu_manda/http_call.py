import requests
from mridu_manda import config



OPEN_WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
IPINFO_URL = "https://www.ipinfo.io/json"


def make_call(indicator, city = " "):
    
    if indicator == 'c':
        params = { }
        
        response = requests.get(IPINFO_URL, params=params)
        response.raise_for_status()
        
        return response
        
    if indicator == 'w':
        
        api = config.get_api_key().get('api_key')
        city = city
        params = {
            "q": city,
            "appid": api,
            "units": "metric"
        }
        
        response = requests.get(OPEN_WEATHER_URL, params=params)
        response.raise_for_status()
        
        return response.json()