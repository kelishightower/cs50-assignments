# test_twttr.py
# Kelis Hightower

# imports the shorten function from twttr
from twttr import shorten


def main():
    test_shorten_case_insensitive()
    test_shorten_numbers()
    test_shorten_punctuation()


# test to see if it can still remove the vowels even with various captial letter in one string
def test_shorten_case_insensitive():
    assert shorten('twitter') == 'twttr'
    assert shorten('TWITTER') == 'TWTTR'
    assert shorten('TwItTeR') == 'TwtTR'

# test to see if numbers are still procces and printed (conserved)


def test_shorten_numbers():
    assert shorten('1234') == '1234'

# test to see if punctuation is process, printed, and conserved


def test_shorten_punctuation():
    assert shorten("!?,.") == '!?,.'


# calls main
if __name__ == "__main__":
    main()
