# test_fuel.py
# Kelis Hightower

# importing necissary funtions
from fuel import convert
from fuel import gauge
import pytest


def main():
    test_convert_gauge_correct_output()
    test_convert_gauge_ValueError()

# in on function test to see that both the cnvert and gauge function retuns the right values (simultaniously)


def test_convert_gauge_correct_output():
    assert convert('1/4') == 25 and gauge(25) == '25%'
    assert convert('99/100') == 99 and gauge(99) == 'F'
    assert convert('1/100') == 1 and gauge(1) == 'E'

# checks to make sure that errors arise when the worng values are inputed or when zero in in the denominator.
# or in other words make sure it dosent allow invlaid inputs to pass through and are getting flagged by errors


def test_convert_gauge_ValueError():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ZeroDivisionError):
        convert('1/0')


# calls main
if __name__ == "__main__":
    main()
