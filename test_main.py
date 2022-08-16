from main import say_hello


def test_default():
    actual = say_hello()
    expected = "Hello stranger"
    assert actual == expected
