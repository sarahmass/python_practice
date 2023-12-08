"""
    CS50P week 5 problem set 5 test bank
    Test the bank.py
"""

from bank import value

def main():
    test_value_mixed_case()
    test_value_lower()
    test_value_all_caps()
    test_value_leading_space()
    test_value_multi_word()
    test_value_oddities()
    test_value_punct()


def test_value_mixed_case():
    assert value("HeLlO") == 0
    assert value("HoWdY") == 20
    assert value("SuP") == 100


def test_value_lower():
    assert value("hello") == 0
    assert value("howdy") == 20
    assert value ("sup") == 100

def test_value_all_caps():
    assert value("HELLO") == 0
    assert value("HOWDY") == 20
    assert value("SUP") == 100

def test_value_leading_space():
    assert value(" hello") == 0
    assert value(" howdy") == 20
    assert value(" sup") == 100

def test_value_multi_word():
    assert value("hello, howdy, how are you?") == 0
    assert value("howdy, hello, how are you?") == 20
    assert value("what's up? howdy, hello") == 100

def test_value_oddities():
    assert value(" ") == 100
    assert value("  1 2 3 ") == 100
    assert value("h e l l 0") == 20
    assert value(" !hello!") == 100

def test_value_punct():
    assert value("hello!") == 0
    assert value("howdy?") == 20
    assert value("what's up?!") == 100


if __name__ == "__main__":
    main()