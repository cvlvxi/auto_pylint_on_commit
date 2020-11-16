"""Module Docstring"""
from stuff.lib import Dog


def test_something():
    """Doc string"""
    assert True

def test_stuff():
    my_dog = Dog("Maxwell", 6)
    assert my_dog.dog_name == "Maxwell"
    my_dog.sit()
    my_dog.roll_over()
