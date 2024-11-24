from functionAdd import add


def test_add():
    assert add(2, 5) == 7
    assert add(10, 6) == 16
    assert add(100,  100) == 200


