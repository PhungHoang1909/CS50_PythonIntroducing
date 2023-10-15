#Lecture 5 - Unit Tests

from hello import hello

def test_hello():
    assert hello() == "Hello, World"

def test_argument():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"Hello, {name}"