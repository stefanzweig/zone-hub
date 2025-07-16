import sys

sys.path.append("..")
from src import singleton


def test_singleton():
    SingleInt = singleton(int)
    a = SingleInt(10)
    b = SingleInt(20)
    assert a is b
    print(a)
