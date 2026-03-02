import json
import requests
import sys
import time
import os
from datetime import date
from mridu_manda import setup_mridumanda, setup_weather_data, ascii_arts
from rich.console import Console
from rich.table import Table



city_weather = None
country = None
weather = None
weather_id = None
temperature = None
feels_like = None
humidity = None
temperature_max = None
temperature_min = None
pressure = None



def main():
    setup_mridumanda.setup()
    setup_weather_data.setup()
    
    if (len(sys.argv) > 1) and (sys.argv[1] == "-m"):
        manual_city() 
    else:
        auto_city()
    
    
def auto_city():
    setup_mridumanda.setup()
    setup_weather_data.setup()
    
    print("Welcome to MriduManda")
    print("Fetching city...")
    time.sleep(1)
    city = get_city()
    path_to_api = os.path.join(os.path.expanduser("~"), ".mridumanda", "api.txt")
    api = None
    
    with open (path_to_api, "r") as file:
        line = file.readline()
        
        if ":" in line:
            key, value = line.strip().split(":", 1)
            api = value
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"
    
    try:
        response = requests.get(url)
    except:
        print("There was an error while fetching weather report!")
        print("Try again later.")
        sys.exit()
    
    time.sleep(1)
    os.system('clear')
    
    if response.status_code == 200:
        access_weather(response.json(), city)
        
    else:
        print("Error:", response.status_code)
    
    weather_choice()


def manual_city():
    setup_mridumanda.setup()
    
    print("Welcome to MriduManda")
    
    city = input("Enter a city: ")
    path_to_api = os.path.join(os.path.expanduser("~"), ".mridumanda", "api.txt")
    api = None
    
    with open (path_to_api, "r") as file:
        line = file.readline()
        
        if ":" in line:
            key, value = line.strip().split(":", 1)
            api = value
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"
    
    try:
        response = requests.get(url)
    except:
        print("There was an error while fetching weather report!")
        print("Try again later.")
        sys.exit()
    
    time.sleep(1)
    os.system('clear')
    
    if response.status_code == 200:
        access_weather(response.json(), city)
        
    else:
        print("Error:", response.status_code)
    
    
    weather_choice()


def access_weather(weather_data, city):
    global city_weather, country, weather_id, weather, temperature, feels_like, humidity, temperature_max, temperature_min, pressure
    
    city_weather = city
    country = weather_data['sys']['country']
    weather_id = weather_data['weather'][0]['id']
    weather = weather_data['weather'][0]['description'].title()
    temperature = weather_data['main']['temp']
    feels_like = weather_data['main']['feels_like']
    humidity = weather_data['main']['humidity']
    pressure = weather_data['main']['pressure']
    temperature_max = weather_data['main']['temp_max']
    temperature_min = weather_data['main']['temp_min']


def get_city():
    try:
        ipinfo_data = requests.get("https://www.ipinfo.io/json")
        city = ipinfo_data.json().get('city')
    except:
        os.system('clear')
        print("There was a problem fetching your home town!")
        print("Kindly try manual city enter option.")
        sys.exit()
    return city


def weather_choice():
    weather_style = input("Enter option (default / one liner / formatted one liner / ascii): ")
    
    if weather_style.lower() == "o":
        print_weather_one_line()
    elif weather_style.lower() == "fo":
        print_formatted_oneliner()
    elif weather_style.lower() == "f":
        print_formatted_weather()
    elif weather_style.lower() == "a":
        print_ascii_weather()
    else:
        print_weather()


def print_weather():
    os.system('clear')
    print(f"City \t\t\t\t : {str.capitalize(city_weather)}")
    print(f"Weather \t\t\t : {weather}")
    print(f"Temperature \t\t\t : {temperature}°C")
    print(f"Feels like \t\t\t : {feels_like}°C")
    print(f"Temperature (Max) \t\t : {temperature_max}°C")
    print(f"Temperature (Min) \t\t : {temperature_min}°C")
    print(f"Humidity \t\t\t : {humidity}")
    print(f"Pressure \t\t\t : {pressure}")
    
    save_weather()


def print_weather_one_line():
    os.system('clear')
    print(f"City: {str.capitalize(city_weather)}   |   Weather: {weather}   |   Temperature: {temperature}°C   |   Pressure: {pressure}")
    
    save_weather()


def print_formatted_oneliner():
    os.system('clear')
    weather_console = Console()
    weather_table = Table(show_header=False, border_style="bold blue")

    weather_table.add_row(f"{str.capitalize(city_weather)}", f"{weather}", f"{temperature}°C", f"{pressure} hPa", style="bold")
    
    weather_console.print(weather_table)
    
    save_weather()
    

def print_formatted_weather():
    os.system('clear')

    weather_console = Console()
    table_title = f"Weather Report for {str.capitalize(city_weather)}, {country}"
    weather_table = Table(show_header=False, border_style="dim")

    weather_table.add_row("Temperature", f"{temperature}°C")
    weather_table.add_row("Humidity", f"{humidity}%")
    weather_table.add_row("Temperature (Max)", f"{temperature_max}°C")
    weather_table.add_row("Temperature (Min)", f"{temperature_min}°C")
    weather_table.add_row("Condition", f"{weather}")
    weather_table.add_row("Pressure", f"{pressure} hPa")

    weather_console.print(table_title, justify="center", style="bold italic")
    weather_console.print(("-" * (len(table_title) - 4)), justify="center")
    weather_console.print(weather_table, justify="center")

    save_weather()


def print_ascii_weather():
    os.system('clear')
    
    ascii = None
    weather_data = [
        " ",
        f"{str.capitalize(city_weather)}, {country}",
        f"{weather}",
        " ",
        f"{temperature}°C",
        f"{humidity}%",
        " ",
        f"{temperature_max}°C \u2b06",
        f"{temperature_min}°C \u2b07",
        f"{pressure} hPa",
        " "
    ]
    
    if 200 <= weather_id < 300:
        ascii = ascii_arts.ascii_arts.thunder
    # elif 300 <= weather_id < 400:
        # condition = ascii_arts.ascii_arts.drizzle // to be implemented
    elif 500 <= weather_id < 600:
        ascii = ascii_arts.ascii_arts.rain
    elif 600 <= weather_id < 700:
        ascii = ascii_arts.ascii_arts.snow
    elif weather_id == 711:
        ascii = ascii_arts.ascii_arts.smoke
    elif weather_id == 731:
        ascii = ascii_arts.ascii_arts.dust
    elif weather_id == 741:
        ascii = ascii_arts.ascii_arts.fog
    elif weather_id == 762:
        ascii = ascii_arts.ascii_arts.ash
    elif weather_id == 771:
        ascii = ascii_arts.ascii_arts.squall
    elif weather_id == 781:
        ascii = ascii_arts.ascii_arts.tornado
    elif weather_id == 800:
        ascii = ascii_arts.ascii_arts.clear_day
    elif 801 <= weather_id < 900:
        ascii = ascii_arts.ascii_arts.clouds
    
    for index, element in enumerate(ascii):
        print(f"{element} \t {weather_data[index]}")



def save_weather():    
    
    setup_weather_data.setup()
    
    weather_report = {"city": str.capitalize(city_weather), "weather_condition": weather, "temperature": temperature, "feels_like": feels_like, "humidity": humidity}
    
    with open(os.path.join(os.path.expanduser("~"), ".mridumanda", "weather.json"), "r+") as file:
        temp_json = json.load(file)
        temp_json[str(date.today())] = weather_report
        file.seek(0)
        json.dump(temp_json, file, indent=4)