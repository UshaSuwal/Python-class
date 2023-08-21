# OOP is an approach of programming in which programs are modeled in the real world-problems.
# OOP stands for Object Oriented Programming language.
# It has two major aspects: Class and Object.

# CLass is blueprint of an object.It has its own attributes known as properties and methods.
# Objects are the instance of a class
# one class can have multiple objects

# There are four major pillar of OOP:
#1. Inheritance
#2. Encapsulation
#3. Polymorphism
#4. Abstraction

class Vehicle:
    engine_type="petrol"    #class attribute

    def __init__(self, number_of_doors,color):   #__init__ is a contructor  # self=v   Vehicle(v,4,"red")   object(v) is sent defaultly so lekhirakhnu pardaina
        self.number_of_doors=number_of_doors   #instance attribute
        self.color=color  #instance attribute
    def description(self):   # here self=v because yo func lai jun object le call gareko xa self chai tei object hunxa.
        return f"vehicle engine is{self.engine_type}. it has {self.number_of_doors} and "\
            f"color is{self.color}"

v=Vehicle(4,"red")
print(v.number_of_doors)  # 4
print(v.color)   # red
print(v.engine_type)  # petrol
print(Vehicle.engine_type)  # petrol    # class attribute can be called from class but instance attribute cant be called by class 
#print(Vehicle.color)   Attribute Error because color is an instance attribute

print(v.description())


# In this vehicle class "engine_type" is class attribute,color and number_of_doors are instance
# attributes and __init__ is a constructor

# Class have properties(variable) and methods(function) which are collectively termed as "attributes"

# Let's set attributes in the objects.
v2=Vehicle(2,"green")    # self=v2 hunxa yeta pani
print(v2.color)  #green
v2.color="blue"
print(v2.color)  #blue
