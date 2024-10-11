# # test_project.py
# # Kelis Hightower


import pytest
from unittest.mock import patch, mock_open
import requests
from project import kelvin_to_fahrenheit, get_temperature, get_feels_like, get_high_temp, get_low_temp, get_rain_description, get_weather_data

# creates a fixed set of data that can be used/referenced when testing


@pytest.fixture
def mock_api_key_file():
    # Patch the built-in open function and simulate reading 'fake_api_key' from a file using a mock open function to open a mock file
    with patch('builtins.open', mock_open(read_data='fake_api_key')) as m:
        yield m


@pytest.fixture
def mock_input():
    # creates a place holder where the inputs are camas,wa,us using the built-in input function call and the side effects are inputs
    with patch('builtins.input', side_effect=['Camas,WA,US', 'temperature']) as m:
        yield m

# sets a fixed request placeholder that can be accessed later


@pytest.fixture
def mock_requests_get():
    # Patch the requests.get function to avoid making real HTTP requests
    # acts as a copycat request.get function to make a fake request to a placeholder HTTP which is assigned to "m"
    with patch('requests.get') as m:
        # Create a mock response object with a predefined JSON response
        # the fake response = the value that is returned when it is called by the mock function
        mock_response = m.return_value
        # ignore and calls from the raise_for_status since there is no HTTP to access
        mock_response.raise_for_status = lambda: None
        # creates a fake data set that can be used when testing functions/ instantiates the return values I call on above
        mock_response.json.return_value = {
            'main': {
                'temp': 300,
                'feels_like': 295,
                'temp_max': 305,
                'temp_min': 290
            },
            'weather': [{'description': 'light rain'}]
        }
        yield m

# Test for the get_weather_data function using the mock fixtures


def test_get_weather_data(mock_api_key_file, mock_input, mock_requests_get):
    # Call the get_weather_data function to see if everything works as expected
    # this will use the following fake inputs to test it
    city_name = 'Camas'
    state_code = 'WA'
    country_code = 'US'
    api_key = 'fake_api_key'
    data = get_weather_data(city_name, state_code, country_code, api_key)

    # Check if the values are correctly fetched and returned
    assert data['main']['temp'] == 300

# tests to make sure the Kelvin --> F works


def test_kelvin_to_fahrenheit():
    # asserting that value passed in will equal the right conversion (with a bit of room for error)
    assert kelvin_to_fahrenheit(290) == pytest.approx(62.33, 0.01)


def test_get_temperature():
    # Mock data to pass to the function
    data = {'main': {'temp': 300}}
    # Call the function and check if the returned string is correct
    result = get_temperature(data)
    # asserts that the result matches with the desired result
    assert result == "It is currently 80.33 degrees Fahrenheit"


def test_get_feels_like():
    # Mock data to pass to the function
    data = {'main': {'feels_like': 295}}
    # Call the function and check if the returned string is correct
    result = get_feels_like(data)
    # asserts that the result matches with the desired result
    assert result == "It feels like 71.33 degrees Fahrenheit"


def test_get_high_temp():
    # Mock data to pass to the function
    data = {'main': {'temp_max': 305}}
    # Call the function and check if the returned string is correct
    result = get_high_temp(data)
    # asserts that the result matches with the desired result
    assert result == "The high temperature is 89.33 degrees Fahrenheit"


def test_get_low_temp():
    # Mock data to pass to the function
    data = {'main': {'temp_min': 290}}
    # Call the function and check if the returned string is correct
    result = get_low_temp(data)
    # asserts that the result matches with the desired result
    assert result == "The low temperature is 62.33 degrees Fahrenheit"


def test_get_rain_description():
    # Mock data to pass to the function
    data = {'weather': [{'description': 'light rain'}]}
    # Call the function and check if the returned string is correct
    result = get_rain_description(data)
    # asserts that the result matches with the desired result
    assert result == "The rain description is: light rain 🌧️"


# calls the main function
if __name__ == "__main__":
    pytest.main()
