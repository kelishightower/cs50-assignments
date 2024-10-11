# app.py
# Kelis Hightower

import requests
import sys

def get_weather_data(city_name, state_code, country_code, api2_key):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{state_code},{country_code}&appid={api2_key}')
    response.raise_for_status()
    return response.json()

def get_info(data, info_requested):
    if info_requested in ["temperature", "temp"]:
        print(get_temperature(data))
    elif info_requested in ["feels like", "feelslike"]:
        print(get_feels_like(data))
    elif info_requested == "high temp":
        print(get_high_temp(data))
    elif info_requested == "low temp":
        print(get_low_temp(data))
    elif info_requested in ["rain description", "rain"]:
        print(get_rain_description(data))
    else:
        print("No valid action entered")

def main():
    try:
        with open('api2_key.txt', 'r') as file:
            api2_key = file.read().strip()
    except FileNotFoundError:
        sys.exit("API key file not found")

    while True:
        try:
            user_input = input("Enter your city,state code,country code ('Example: Camas,WA,US'): ")
            city_name, state_code, country_code = user_input.split(",")
            data = get_weather_data(city_name, state_code, country_code, api2_key)
            break
        except ValueError:
            print("Please enter the city,state code,country code in the correct format.")
            continue
        except requests.exceptions.HTTPError as err:
            if err.response.status_code == 404:
                print("Error retrieving data for the city, please check your input and try again.")
                continue

    while True:
        try:
            info_requested = input("Awesome, what would you like to know about that city?: ").lower()
            get_info(data, info_requested)
        except EOFError:
            print("\nExiting...")
            break

def get_temperature(data):
    temp = data['main']['temp']
    fahrenheit_temp = kelvin_to_fahrenheit(temp)
    return f"It is currently {fahrenheit_temp:.2f} degrees Fahrenheit"

def kelvin_to_fahrenheit(temp):
    return (temp - 273.15) * 1.8 + 32

def get_feels_like(data):
    feels_like = data['main']['feels_like']
    feels_like_fahrenheit = kelvin_to_fahrenheit(feels_like)
    return f"It feels like {feels_like_fahrenheit:.2f} degrees Fahrenheit"

def get_high_temp(data):
    high_temp = data['main']['temp_max']
    high_temp_fahrenheit = kelvin_to_fahrenheit(high_temp)
    return f"The high temperature is {high_temp_fahrenheit:.2f} degrees Fahrenheit"

def get_low_temp(data):
    low_temp = data['main']['temp_min']
    low_temp_fahrenheit = kelvin_to_fahrenheit(low_temp)
    return f"The low temperature is {low_temp_fahrenheit:.2f} degrees Fahrenheit"

def get_rain_description(data):
    try:
        rain_description = data['weather'][0]['description']
        if "rain" in rain_description:
            return f"The rain description is: {rain_description} 🌧️"
        else:
            return "Doesn't appear to be any rain 🌞"
    except KeyError:
        return "There is no rain description available."

if __name__ == "__main__":
    main()
