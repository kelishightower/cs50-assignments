# # # project.py
# # # Kelis Hightower

# imports request in order to access data from the api
import requests
# imports sys so we can preform sys exits
import sys

# creates a function that gets the weather data from the OpenWeatherMap api


def get_weather_data(city_name, state_code, country_code, api_key):
    # creates a get request to the API with arguments passed into the function about to create a valid acceabile link
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={
                            city_name},{state_code},{country_code}&appid={api_key}')
    # Raises a HTTP error is for some reason the request dosent work meaning the link is invalid (in other words raises 404 error)
    response.raise_for_status()
    # returns the response as a json. object
    return response.json()

# creates a function that takes in the data gathered form the API and the useres in put when prompted


def get_info(data, info_requested):
    # a series of if staments that takes the useres request a retuns the coresponding data (using a paticular function that does the returning)
    # for example (user input = temp--> calls the get_tempautre function ---> ultimely print the temp to the terminal)
    # same logic applies for all additional functions below, or a the key word "list" to print avaible functions
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
    elif info_requested in ["list", "List"]:
        print(list())
    # if the user types in something worng or random it tell the user their input is not valid
    else:
        print("No valid action entered")

# creates a main function


def main():
    # attempts to open a pre-established file called "api_key.txt" as a read file to read the api key listed
    try:
        with open('api_key.txt', 'r') as file:
            # reads the file and strips any blank space that may be in the file
            api_key = file.read().strip()
    # if the file isnt fount except the error by exiting the program and saying the follwoing message
    except FileNotFoundError:
        sys.exit("API key file not found")

    while True:
        # Witin a while loop prompt the user for a location in the desired format
        try:
            # try to prompt the user...
            user_input = input(
                "Enter your city,state code,country code ('Example: Camas,WA,US'): \n")
            # try to take the input and split it by the camas into three different varibles (city,state,country)
            city_name, state_code, country_code = user_input.split(",")
            # creates a data varible that calls the get weahter funtion passing in the three vars that we just created... this allows us to form a valid api link
            data = get_weather_data(city_name, state_code, country_code, api_key)
            # if this all works break out of this loop
            break
        # excpet a vlaue error by printing the following and repromting the user to try again (continue untill entered the desired format)
        except ValueError:
            print("Please enter the city,state code,country code in the correct format.")
            continue
        # Also except a HTTP error or a 404 error which indicated some sort of data retrival issues
        except requests.exceptions.HTTPError as err:
            # if the error is a 404 error print the following and reprompt (continue)
            if err.response.status_code == 404:
                print("Error retrieving data for the city, please check your input and try again.")
                continue
    # in another loop...
    while True:
        try:
            # try to get info_requested from the user and converts it to lower to make it case insensitive
            info_requested = input(
                "What would you like to know? (press contorl d to exit) or List for valid actions: ").lower()
            # try to call get into using "data (gathered previously)" and the varible we just created (info_gathered)
            get_info(data, info_requested)
        # if the user presses controll D print the following and exit the program
        except EOFError:
            print("\nBye bye!")
            break
# creates a function that simply return a list of avaible function that can be called using the info_requested intput


def list():
    return "temp/tempature = send back the current tempature\nrain = current rain description\n low temp = low temp for day\n high temp = high temp for the day\n feels like = what temp it feels like currenlty"


def get_temperature(data):
    # gets the temperature in Kelvin from the data
    temp = data['main']['temp']
    # converts the temperature from kelvin to Fahrenheit calling the kelvin_to_fahrenhit function
    fahrenheit_temp = kelvin_to_fahrenheit(temp)
    # return the infomation in the desired format (rounding the value to two decimal places out)
    return f"It is currently {fahrenheit_temp:.2f} degrees Fahrenheit"

# a function to convert temperature from Kelvin to Fahrenheit


def kelvin_to_fahrenheit(temp):
    return (temp - 273.15) * 1.8 + 32

# a function that retives the feels like data form api


def get_feels_like(data):
    # gets the "feels like" temperature from api
    feels_like = data['main']['feels_like']
    # converts it from K to F
    feels_like_fahrenheit = kelvin_to_fahrenheit(feels_like)
    # return the infomation in the desired format (rounding the value to two decimal places out)
    return f"It feels like {feels_like_fahrenheit:.2f} degrees Fahrenheit"

# a function that retives the high temp data form api


def get_high_temp(data):
    # gets the "high temp" from api
    high_temp = data['main']['temp_max']
    # converts it from K to F
    high_temp_fahrenheit = kelvin_to_fahrenheit(high_temp)
    # return the infomation in the desired format (rounding the value to two decimal places out)
    return f"The high temperature is {high_temp_fahrenheit:.2f} degrees Fahrenheit"

# a function that retives the low temp data form api


def get_low_temp(data):
    # gets the "low temp" from api
    low_temp = data['main']['temp_min']
    # converts it from K to F
    low_temp_fahrenheit = kelvin_to_fahrenheit(low_temp)
    # return the infomation in the desired format (rounding the value to two decimal places out)
    return f"The low temperature is {low_temp_fahrenheit:.2f} degrees Fahrenheit"

# a function that retives the rain decription data form api


def get_rain_description(data):
    try:
        # gets rain decription from the API
        rain_description = data['weather'][0]['description']
        # if rain is in the description return the data with a rain cloud on the end
        if "rain" in rain_description:
            return f"The rain description is: {rain_description} 🌧️"
        # if it dosent have rain return it with a sun on the end
        else:
            return "Doesn't appear to be any rain 🌞"
    # except a KeyError and return the following
    except KeyError:
        return "There is no rain description available."


# calls the main function
if __name__ == "__main__":
    main()
