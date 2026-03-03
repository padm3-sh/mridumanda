import os
from mridu_manda import config, ascii_arts
from rich.console import Console
from rich.table import Table



def display(weather):
    weather_style = input("Enter option (default / one liner / formatted / formatted one liner / ascii): ")
    
    if weather_style.lower() == "o":
        print_weather_one_line(weather)
    elif weather_style.lower() == "fo":
        print_formatted_oneliner(weather)
    elif weather_style.lower() == "f":
        print_formatted_weather(weather)
    elif weather_style.lower() == "a":
        print_ascii_weather(weather)
    else:
        print_weather(weather)
    
    config.save_weather(weather)


def print_weather(weather):
    os.system('clear')
    print(f"City \t\t\t\t : {weather[0]}")
    print(f"Weather \t\t\t : {weather[3]}")
    print(f"Temperature \t\t\t : {weather[4]}°C")
    print(f"Feels like \t\t\t : {weather[5]}°C")
    print(f"Temperature (Max) \t\t : {weather[8]}°C")
    print(f"Temperature (Min) \t\t : {weather[9]}°C")
    print(f"Humidity \t\t\t : {weather[6]}")
    print(f"Pressure \t\t\t : {weather[7]}")


def print_weather_one_line(weather):
    os.system('clear')
    print(f"City: {weather[0]}   |   Weather: {weather[3]}   |   Temperature: {weather[4]}°C   |   Pressure: {weather[7]}")


def print_formatted_oneliner(weather):
    os.system('clear')
    weather_console = Console()
    weather_table = Table(show_header=False, border_style="bold blue")
    
    weather_table.add_row(f"{weather[0]}", f"{weather[3]}", f"{weather[4]}°C", f"{weather[7]} hPa", style="bold")
    
    weather_console.print(weather_table)


def print_formatted_weather(weather):
    os.system('clear')
    
    weather_console = Console()
    table_title = f"Weather Report for {weather[0]}, {weather[1]}"
    weather_table = Table(show_header=False, border_style="dim")
    
    weather_table.add_row("Temperature", f"{weather[4]}°C")
    weather_table.add_row("Humidity", f"{weather[6]}%")
    weather_table.add_row("Temperature (Max)", f"{weather[8]}°C")
    weather_table.add_row("Temperature (Min)", f"{weather[9]}°C")
    weather_table.add_row("Condition", f"{weather[3]}")
    weather_table.add_row("Pressure", f"{weather[7]} hPa")
    
    weather_console.print(table_title, justify="center", style="bold italic")
    weather_console.print(("-" * (len(table_title) - 4)), justify="center")
    weather_console.print(weather_table, justify="center")


def print_ascii_weather(weather):
    os.system('clear')
    
    ascii = None
    weather_data = [
        " ",
        f"{weather[0]}, {weather[1]}",
        f"{weather[3]}",
        " ",
        f"{weather[4]}°C",
        f"{weather[6]}%",
        " ",
        f"{weather[8]}°C \u2b06",
        f"{weather[9]}°C \u2b07",
        f"{weather[7]} hPa",
        " "
    ]
    
    if 200 <= weather[2] < 300:
        ascii = ascii_arts.ascii_arts.thunder
    # elif 300 <= weather[2] < 400:
        # condition = ascii_arts.ascii_arts.drizzle // to be implemented
    elif 500 <= weather[2] < 600:
        ascii = ascii_arts.ascii_arts.rain
    elif 600 <= weather[2] < 700:
        ascii = ascii_arts.ascii_arts.snow
    elif weather[2] == 711:
        ascii = ascii_arts.ascii_arts.smoke
    elif weather[2] == 731:
        ascii = ascii_arts.ascii_arts.dust
    elif weather[2] == 741:
        ascii = ascii_arts.ascii_arts.fog
    elif weather[2] == 762:
        ascii = ascii_arts.ascii_arts.ash
    elif weather[2] == 771:
        ascii = ascii_arts.ascii_arts.squall
    elif weather[2] == 781:
        ascii = ascii_arts.ascii_arts.tornado
    elif weather[2] == 800:
        ascii = ascii_arts.ascii_arts.clear_day
    elif 801 <= weather[2] < 900:
        ascii = ascii_arts.ascii_arts.clouds
        
    for index, element in enumerate(ascii):
        print(f"{element} \t {weather_data[index]}")