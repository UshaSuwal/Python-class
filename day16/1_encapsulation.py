# Encapsulation is the process of data hiding in OOP approach of programming
# We can make the attributes private,public or protected.
# In python, protected members can be created using a single underscore "_" and private members can be 
# created using double underscore "__"

class Vehicle:
    _color="blue"   #this is protected propertiy
    __milage=50     #this is private property

    def __init__(self,doors,speed):
        self._doors=doors  #protected member
        self._speed=speed  #protected member
    
    def description(self):
        return f"color = {self._color} Doors = {self._doors} and speed = {self._speed}"
    
    def set_color(self,color):
        self._color=color
    def get_color(self):
        return self._color

v1=Vehicle(4,120)
print(v1._color)  # Accesing protected member outside the class which is not recommended
print(v1.description())
v1.set_color("green")
print(v1.get_color())    # green


# protected member of a class are meant to be used within a class or in their children class only
# they are not meant to be used outside a class
# Python is not strict in OOP approach. So it allows protected members to be accessed even outside the
# class. But, this is not recommended for developers as it doesn't follow proper convention

# Private property is not accessible outside the class or in children classes
# print(v1.__milage)  it raises attribute error because __milage is private property
print(dir(v1))
print(v1._Vehicle__milage)   #50 Accessing private property
# Though __milage is private property, we can access this by _Vehicle__milage. This is also called
# "name mangling" in Python