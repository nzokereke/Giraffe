"""
   -------- Object Oriented Programming --------
   1. oop breaks a program into objects that interact with each other
   2. these objects are created from templates known as 'classes'
   3. 4 pillars of oo - its important that you understand this

   ---------classes -----------
   - to create a class you use the key word 'class' followed by the name of the class
     a class is declared as follows - class CarParts:
   - in python PascalCasing is the convention used in naming a class e.g CarParts
   - a class consists of variables and functions
   - functions within a class are called 'methods'
   - a class is used to store related data and methods

"""
''' ------------ elements of a class -------------
   1. _init_ :  
              (a) a special method called when creating an object of a class 
              (b) used to initialise the variables
   2. instance variables:  
                   (a) make, model, transmission e.t.c are referred to as 'instance' variables of the class 'Car'.
                   (b) is an attribute defined inside the constructor.
   3. self: 
           (a) used in method definitions and in variable initialization 
           (b) used to access the attributes and methods of the class
           
   4. _repr_ : another special method used to format and return readable values contained in the variables
   
   5. calculate_value: is a method that will return the value of a car factoring in a yearly 10% depreciation 
           
'''


class Car(object):
    def __init__(self, make, model, transmission, fuel, value):  # creates  the attributes of the class
        self.make = make  # here we are telling python that the variables has the same value as the attributes
        self.model = model  # i.e self.<any_variable_name> = class attribute e.g. make, model
        self.transmission = transmission
        self.fuel = fuel
        self.value = value

    def __repr__(self):
        return "Car(%s, %s, %s, %s, %d)" % \
               (self.make, self.model, self.transmission, self.fuel, self.value)

    def calculate_value(self):
        price = self.value
        year = int(input('how old is the car: '))
        while year > 0:
            percent = price * 10 / 100
            price = price - percent
            self.value = price
            year -= 1
        return self.value


''' creating an instance of the class 'Car' '''

# alpha = Car('mini', 'cooper', 'automatic', 'petrol', 0)  # alpha is the new instance
#
# print(alpha.value)
# alpha.calculate_value()  # calling the method
# print(alpha)

'''  ------------------------    creating a child class   ------------------------- 
    1. Hybrid(Car) - here, we are indicating that Hybrid is a subclass of Car by adding Car to the parentheses
    2. def __init__(self,...) - attributes for the child class
    3. super() function  - allows the child class to call methods and use attributes of the parent class
'''


class Hybrid(Car):
    def __init__(self, make, model, transmission, fuel, value, type_of_hybrid):
        super().__init__(make, model, transmission, fuel, value)
        self.type_of_hybrid = type_of_hybrid

    def __repr__(self):
        return "Car(%s, %s, %s, %s, %d, %s)" % \
               (self.make, self.model, self.transmission, self.fuel, self.value,
                self.type_of_hybrid)


class Hyper(Car):
    def __init__(self, make, model, transmission, fuel, value, speed, cylinder):
        super().__init__(make, model, transmission, fuel, value)
        self.speed = speed
        self.cylinder = cylinder


h = Hyper('mini', 'cooper', 'auto', 'petrol', 15000, 100, 6)

h.calculate_value()
print(h)
