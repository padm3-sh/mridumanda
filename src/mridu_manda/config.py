from datetime import date
from pathlib import Path
import json
import os
import sys



API_FILE = Path("~/.mridumanda/api.txt").expanduser()
WEATHER_FILE = Path("~/.mridumanda/weather_data.json").expanduser()


def get_api_key():
    
    if not API_FILE.exists():
        setup_mrdmnd_api()
    
    api = { }
    
    for line in API_FILE.read_text().splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            api[key.strip()] = value.strip()
            
            if len(value) < 32:
                print("The API key looks invalid!")
                print("Kindly, enter the API key again")
                setup_mrdmnd_api()
    
    return api


def setup_mrdmnd_api():
    
    os.system("mkdir -p $HOME/.mridumanda")
    
    api_key = input("Enter your api key: ")
    
    API_FILE.write_text(f"api_key: {api_key}")
    
    print("API key saved successfully")
    print("Rerun the program again to enjoy the service.")
    sys.exit(0)


def setup_mrdmnd_data():
    
    if not WEATHER_FILE.exists():
        with WEATHER_FILE.open("x") as file:
            json.dump({}, file, indent=4)


def save_weather(weather):    
    
    setup_mrdmnd_data()
    
    weather_report = {"location": f"{weather[0]}, {weather[1]}" , "weather_condition": weather[3], "temperature": weather[4], "feels_like": weather[5], "humidity": weather[6]}
    
    with WEATHER_FILE.open("r+") as file:
        temp_json = json.load(file)
        temp_json[str(date.today())] = weather_report
        file.seek(0)
        json.dump(temp_json, file, indent=4)
        file.truncate()