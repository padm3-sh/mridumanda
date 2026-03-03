import sys
import time
from mridu_manda import fetch_city, http_call, parse_weather, print_weather



def main():
    
    print("Welcome to MriduManda")
    time.sleep(1)
    print("A simple CLImate application!\n")
    time.sleep(1)
    
    city = fetch_city.fetch_city(sys.argv)
    
    weather_report = http_call.make_call('w', city)
    
    formatted_weather = parse_weather.weather_access(weather_report)
    
    print_weather.display(formatted_weather)