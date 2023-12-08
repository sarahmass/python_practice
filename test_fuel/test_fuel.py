"""
    CS50P Week 5 problem set 5:
    test fuel.py from week 3 with the following constraints:
        - In a file called fuel.py, reimplement Fuel Gauge from Problem Set 3, restructuring your code per the below, wherein:

            * convert expects a str in X/Y format as input, wherein each of X and Y is an integer, and returns that fraction
              as a percentage rounded to the nearest int between 0 and 100, inclusive. If X and/or Y is not an integer, or
              if X is greater than Y, then convert should raise a ValueError. If Y is 0, then convert should raise a
              ZeroDivisionError.

            * gauge expects an int and returns a str that is:
                "E" if that int is less than or equal to 1,
                "F" if that int is greater than or equal to 99,
                and "Z%" otherwise, wherein Z is that same int
"""
import pytest
from fuel import convert, gauge

def test_convert_div_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_convert_valid_inputs():
    assert convert("0/4") == 0
    assert convert("1/2") == 50
    assert convert("1/1") == 100

def test_convert_value_errors():
    with pytest.raises(ValueError):
        # x not an int
        convert("1.2/2")
    with pytest.raises(ValueError):
        # y not an int:
        convert("2/2.2")
    with pytest.raises(ValueError):
        # neither x nor y are ints
        convert("1.2/1.3")
    with pytest.raises(ValueError):
        # y is less than x
        convert("2/1")
    with pytest.raises(ValueError):
        # no fraction entered
        convert("2")


# def test_convert_return_type():
#     assert type(convert("1/2")) is int

#    # with pytest.raises(TypeError):
#         # input not a str
#      #   convert(1/2)

def test_gauge():
    # Check Empty and boundary
    assert gauge(1) == "E"

    assert gauge(0) == "E"
    assert gauge(2) == "2%"
    assert gauge(50) != "50"


    # Check Full and boundary
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(98) == "98%"

# def test_guage_raise_errors():
#     with pytest.raises(TypeError):
#          gauge("99")
#     with pytest.raises(ValueError):
#          gauge(101)
#     with pytest.raises(ValueError):
#          gauge(-1)


def main():
    test_convert_div_zero()
    test_convert_valid_inputs()
    test_convert_value_errors()
    #     test_convert_return_type()
    test_gauge()
    #     #test_guage_raise_errors()


if __name__ == "__main__":
    main()