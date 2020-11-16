"""Module docstring"""

class Dog:
    """Class docstring"""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.dog_name = name
        self.dog_age = age
        self.name = "Rambo"
        self.age = 12

    def sit(self):
        '''docstring'''
        print(f"{self.dog_name} is now sitting")

    def roll_over(self):
        '''docstring'''
        print(f"{self.dog_age} rolled over!")


