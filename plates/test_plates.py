# test_plates.py
# Kelis Hightower

# import the is_vaid function from plates
from plates import is_valid


def main():
    test_is_valid_length()
    test_is_valid_first_two_letters()
    test_is_valid_first_num_zero()
    test_is_valid_middle_numbers()
    test_is_valid_no_alpha()

# test the length in charcters of the inputed plate


def test_is_valid_length():
    assert is_valid('AAA222') == True
    assert is_valid('AAAAAAAAAAAAAA') == False
    assert is_valid('A') == False
    assert is_valid('AA') == True

# test that the first two charcter values must be letters of the inputed plate


def test_is_valid_first_two_letters():
    assert is_valid('AA2344') == True
    assert is_valid('A32344') == False
    assert is_valid('1ABDF4') == False


# tests that the first numbers entered is greater than zero

def test_is_valid_first_num_zero():
    assert is_valid('ABE350') == True
    assert is_valid('ABER05') == False

# test to make sure that any numbers entered are on the end of the plate value / can not be followed by a letter


def test_is_valid_middle_numbers():
    assert is_valid('AAA222') == True
    assert is_valid('AAA22A') == False
# test that the inputed plate only contains numbers and letters


def test_is_valid_no_alpha():
    assert is_valid("AB-+") == False


if __name__ == "__main__":
    main()
