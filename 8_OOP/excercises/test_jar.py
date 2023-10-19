import pytest
import jar

def test_jar():
    j = jar.Jar(10)
    assert j.capacity == 10
    assert j.size == 0
    assert str(j) == ""

    j.deposit(5)
    assert j.size == 5
    assert str(j) == "🍪🍪🍪🍪🍪"

    j.withdraw(3)
    assert j.size == 2
    assert str(j) == "🍪🍪"

def test_jar_errors():
    with pytest.raises(ValueError):
        jar.Jar(-1)

    j = jar.Jar(10)
    with pytest.raises(ValueError):
        j.deposit(-1)

    with pytest.raises(ValueError):
        j.deposit(11)

    with pytest.raises(ValueError):
        j.withdraw(-1)

    with pytest.raises(ValueError):
        j.withdraw(1)
