'''
    CS50p Week 5 problem set 5: test_twttr:
    After implementing twttr.py again but with the shorten function
    We need to write tests for twttr.py
'''

from twttr import shorten


def main():
    test_shorten_mixed_case()
    test_shorten_lttr_num()
    test_shorten_all_num()
    test_shorten_all_lower()
    test_shorten_all_cap()
    test_shorten_no_vowel()
    test_shorten_all_vowel()


def test_shorten_mixed_case():
    assert shorten("TwITtEr") == "TwTtr"

def test_shorten_lttr_num():
    assert shorten("CS50P") == "CS50P"

def test_shorten_all_num():
    assert shorten("1234567890") == "1234567890"

def test_shorten_all_lower():
    assert shorten("hello")

def test_shorten_all_cap():
    assert shorten("HELLO") == "HLL"

def test_shorten_no_vowel():
    assert shorten("TWTTR") == "TWTTR"

def test_shorten_all_vowel():
    assert shorten("aeiou") == ''

def test_shorten_punct():
    assert shorten("? twitter! $&#.,;:") == "? twttr! $&#.,;:"

if __name__ == "__main__":
    main()