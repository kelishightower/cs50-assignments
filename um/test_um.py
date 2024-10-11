# test_um.py
# Kelis Hightower

# get the count function from the um file

from um import count

# calls all the function


def main():
    test_count_1()
    test_count_2()
    test_count_0()

# test to make sure that certian input values return 1 cause insensitively


def test_count_1():
    assert count("um") == 1
    assert count("um wassup") == 1
    assert count("UM") == 1
    assert count("uM") == 1

# test to make sure that certian input values return 2 cause insensitively


def test_count_2():
    assert count("um Um") == 2
    assert count("um um I don't like bum") == 2
# test to make sure that certian input values return 0 cause insensitively


def test_count_0():
    assert count("ummmmmm") == 0
    assert count("bum") == 0
    assert count("GRumP") == 0


# calls main
if __name__ == "__main__":
    main()
