# test_seasons.py
# Kelis Hightower

# imports the total_minutes function from seasons
from seasons import total_minutes
import pytest

# creates a mian to call our test functions


def main():

    test_total_minutes_Invalid()

# test to make sure our invlaid dates return invalid


def test_total_minutes_Invalid():
    # invalid date should return invalid
    assert total_minutes(23, 1, 2004) == "Invalid date"


# calls main
if __name__ == "__main__":
    main()
