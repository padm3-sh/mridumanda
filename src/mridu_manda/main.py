import requests
import json
import os


def main():
    print("Welcome to MriduManda")
    city = input("Enter city name: ")
    path_to_config = os.path.join(".sanctum", "config.json")
    
    with open (path_to_config, "r") as file:
        config = json.load(file)
        
    api = config['api_key']
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        weather_data = response.json()
        print(f"Weather in {city}: {weather_data['weather'][0]['description']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
    else:
        print("Error:", response.status_code)
