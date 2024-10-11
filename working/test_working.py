# Kelis Hightower
# test_working.py

# imports the convert function from the working file
from working import convert
# imports py test libray so we can test the following
import pytest


# making a claim that the input of ("9 AM to 5 PM") should indeed equal "09:00 to 17:00"
# Do we get the intended output with the right format?


def test_convert_correct_time():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

# Our code in the working file should raise a Value error whith the input of "23 AM to 8 PM"
# Checking to see out code is selective enough with our hour input
# out of range/not a valid hour (for the morning)


def test_convert_incorrect_hours():
    with pytest.raises(ValueError):
        convert("23 AM to 8 PM")

# Same as above but now testing out minutes (out of range or not a valid minute)
# out code should raise a Value Error when "12:99 AM to 5 PM" is inputed... did it catch it?


def test_convert_incorrect_minutes():
    with pytest.raises(ValueError):
        convert("12:99 AM to 5 PM")
# Out code it designed to have a key word to in between times
# Without it, it should raise a Value Error


def test_convert_no_to():
    with pytest.raises(ValueError):
        convert("11 AM 9 PM")

# Our code aslo expects some sort of indeifty word follwoing our times (AM or PM)
# without it, it should raise a Value Error


def test_convert_invalid_time_format():
    with pytest.raises(ValueError):
        convert("8 AM to 12")
