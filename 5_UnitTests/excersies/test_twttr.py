from twttr import shorten

def test_do_argument():
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"

def test_dontdo_argument():
    assert("CS50") == "CS50"

