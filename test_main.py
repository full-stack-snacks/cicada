from main import say_hello


def test_default():
    actual = say_hello()
    expected = "Hello stranger"
    assert actual == expected


def test_with_arg():
    actual = say_hello("neighbor")
    expected = "Hello neighbor"
    assert actual == expected
