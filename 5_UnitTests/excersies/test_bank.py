from bank import value

def test_0dollar():
    assert value("Hello") == "$0"
    assert value("Hello, Newman") == "$0"

def test_20dollars():
    assert value("How you doing?") == "$20"

def test_100dollars():
    assert value("What's happening?") == "$100"