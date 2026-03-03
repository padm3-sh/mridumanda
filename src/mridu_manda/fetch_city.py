import os
import sys
from mridu_manda import http_call



def auto_city():
    
    print("Detecting your home town...")
    
    try:
        ipinfo_data = http_call.make_call('c')
        city = ipinfo_data.json().get('city')
    except:
        os.system('clear')
        print("There was a problem fetching your home town!")
        print("Kindly try manual city enter option.")
        sys.exit()
    
    return city


def manual_city():
    
    city = input("Enter a city: ")
    
    return city


def fetch_city(arguments):
    if len(arguments) > 1 and arguments[1] == "-m":
        return manual_city()
    return auto_city()