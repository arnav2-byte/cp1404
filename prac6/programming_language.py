"""
Estimated time:
Starting time: 2:15 pm
Finishing time:4:15 pm
Actual recorded time: 120 MIN
"""
class ProgrammingLanguages:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year):    # it creates the fields and set them to the parameters
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):   #returns True/False if the programming language is dynamically typed or not.
        return self.typing.lower() == "dynamic"

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, first appearence was {self.year}"