'''  ----------- child class -------
     Here we are importing the class 'Canine' and creating the child class Wolves from the parent class 'Canine'
     1. a child class can inherit the attributes and call the methods the parent class
     2. super() function allows the child class to access the attributes and methods of the parent class
'''

from canine import Canine


class Wolves(Canine):
    def __init__(self, genus, mammal, origin, colour):
        self.origin = origin
        self.colour = colour
        super().__init__(genus, mammal)
