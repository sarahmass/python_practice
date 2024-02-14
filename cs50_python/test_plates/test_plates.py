"""
    cs50p week 5 problem set 5
    test plats from week 2
    - “All vanity plates must start with at least two letters.”
        - “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
        - “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an
            acceptable … vanity plate; AAA22A would not be acceptable.
        - The first number used cannot be a '0'.”
        - “No periods, spaces, or punctuation marks are allowed.”
"""

from plates import is_valid


def main():
    test_is_valid_strts_w_2_lttrs()
    test_is_valid_nums_placement()
    test_is_valid_0_not_frst()
    test_is_valid_only_alphanum()
    test_is_valid_lngth()

def test_is_valid_strts_w_2_lttrs():
    # All vanity plates must start with at least two letters.
    assert is_valid("WW")
    assert not is_valid("12")
    assert not is_valid("W1")
    assert not is_valid("1W")


def test_is_valid_nums_placement():
    # Numbers cannot be used in the middle of a plate
    assert is_valid("WW1234")
    assert not is_valid("WW123W")
    assert not is_valid("WWWW1W")
    assert not is_valid("123456")
    assert not is_valid("ww01234")
    assert not is_valid("1ww023")
    assert is_valid("WW10")
    assert not is_valid("WW10W12")


def test_is_valid_0_not_frst():
    # The first number used cannot be a '0'
    assert not is_valid("WW0")
    assert is_valid("WW10")

def test_is_valid_only_alphanum():
    # No periods, spaces, or other punctuations
    assert not is_valid("WW 123")
    assert not is_valid("WW!")
    assert not is_valid("WW3.14")
    assert is_valid("ABC123")

def test_is_valid_lngth():
    # length must satisfy 2 <= len <= 6
    assert not is_valid("W")
    assert not is_valid("ZZYYXXW")
    assert is_valid("ABCDEF")




if __name__ == "__main__":
    main()
