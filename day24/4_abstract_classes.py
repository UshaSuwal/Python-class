# The classes which cant be instantiated are called abstract classes
# object banauna namilne class
# This is created using "ABC" module from Python built-in
# main motive just to make child inherit  the feature.

from abc import ABC, abstractmethod

class Animal(ABC):   # Animal is abstract class
    #This is an abstract class
    def sleep(self):
        print("I sleep at night")

    @abstractmethod
    def sound(self):     # this must be over write by the child class. decorator must be over write by child 
        pass


class Dog(Animal):
    def sound(self):
        print("I bark")  #over writing

class Cow(Animal):
    def sound(self):
        print("I mhooo")  #over writeing

d=Dog()
d.sound()
d.sleep()
c=Cow()
c.sound()
c.sleep()