# test_numb3rs.py
# Kelis Hightower

# get the validate function from the numbers file
from numb3rs import validate


def main():
    test_validate_returns_true()
    test_validate_returns_false()

# test to see that certian inputs evalute to true


def test_validate_returns_true():
    assert validate("225.225.225.225") == True
    assert validate("13.93.9.225") == True

# tests to see that certian inputs evalute to false


def test_validate_returns_false():
    assert validate("13.93.9") == False
    assert validate("13.93.9.500") == False
    assert validate("13.93.9.256") == False


# calls main
if __name__ == "__main__":
    main()
