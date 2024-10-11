# test_bank.py
# Kelis Hightower
from bank import value


def main():
    test_value_starts_with_hello()
    test_value_starts_with_h()
    test_value_no_h_or_hello()

# test when the value starts with hello with various forms of capital letters


def test_value_starts_with_hello():
    assert value('HELLO') == 0
    assert value('HeLLo') == 0
    assert value('hello') == 0

# test when the value starts with 'h' with various forms of capital letters


def test_value_starts_with_h():
    assert value('Hi') == 20
    assert value('hey') == 20

# test when the value doesent start with an h or a hello (should output 100)


def test_value_no_h_or_hello():
    assert value('bello') == 100
    assert value('wassup') == 100


# call main
if __name__ == "__main__":
    main()
