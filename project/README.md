# Weather App Project
#### Video Demo:  <https://www.loom.com/share/659e1b72aed64b11a22db486a6fccd24?sid=f4112694-7503-458e-969a-60e4c2548482>
#### Description:

## Overview

This project contains one script titled `project.py` which is designed to call an API key from an embedded text file and retrieve specific data based on the user's input. For example, temperature, rain, low, high, etc. This data/api contains information about the current weather conditions from anywhere in the world which can be accessed by the specified location provided by the user (in the desired format/location codes) followed by what piece of information they want to know (such as the listen examples earlier). The user can interact with these functions to receive information as many times as they would like until they hit 'Control + D' to exit the program. They can also enter "List" for a list of infomation they can access and how.

### Design Process

One of the first things I had to design for this project was how to get information from the user. I ended up asking them for what location they wanted information from as my first prompt. I debated asking the user what type of info they wanted on the same line/ in the same input, but I found it easier to manipulate if I separated it into two different input prompts. Secondly, I debated using system arguments to collect information but I felt that it would be easier to loop later on if I just implemented it within the actual project using an input function. However, the idea of re-prompting the user for additional inputs came later in my process. I originally had it exit after it returned the required information but I figured that most people want to know multiple things about the weather such as the highest temp and the rain at once. I felt it was too redundant to keep asking the user for the location each time they wanted to know an additional piece of weather info. As far as some small design features, I decided to incorporate a few emojis into the program depending on if the rain description said it was raining or not just for a bit of aesthetic appeal. Overall I learned a few new things during this process. One of the ones that stuck out was how to create an error detection for a failed HTTP request or a 404 error. I knew what it was but how to implement it into a try-except function was hard. I found it to be a bit different than our usual error detentions so it took a bit of outside research to figure out. Secondly creating my own API key file and accessing it correctly was a whole journey within itself. So while it may seem like a basic app/program to run there were a lot of small things that I learned to make it run the way I wanted to in a practical/applicable way.

### Testing

I felt that the testing process created the biggest learning curve for me. Since I was accessing an API/ requested data with a majority of my functions in my root program I quickly realized that these test functions would have to look different than ones I’ve created in the past. But, with a lot of research and some small outside help, I was able to figure out how to test my program with a "mock" data set using unittest.mock, mock_open, and patch. I learned how to create placeholders for things like API keys and HTTP links and how to access my mock data in each of my sub-test functions along with terminology like fixtures and patches in this context. Once I figured out how to properly establish and access my program the rest of the testing functions came pretty intuitively, I just had to remember to give it enough mock inputs for the functions I was trying to test.

#### Functions

- **`get_weather_data(city_name, state_code, country_code, api_key)`**: Makes an API request to fetch weather data for the specified location.
- **`get_info(data, info_requested)`**: Determines what weather information to retrieve and prints it.
- **`main()`**: The main function that handles user inputs and interactions.
- **`get_temperature(data)`**: Returns the current temperature in Fahrenheit.
- **`kelvin_to_fahrenheit(temp)`**: Converts a temperature from Kelvin to Fahrenheit.
- **`get_feels_like(data)`**: Returns the feels-like temperature in Fahrenheit.
- **`get_high_temp(data)`**: Returns the high temperature of the day in Fahrenheit.
- **`get_low_temp(data)`**: Returns the low temperature of the day in Fahrenheit.
- **`get_rain_description(data)`**: Returns a description of the rain, if available.
- **`list()`**: Returns a list of valid inputs/info requests.

#### Usage

1. Ensure you have an `api_key.txt` file containing your OpenWeatherMap API key.
2. Run the script:
   ```bash
   python project.py
