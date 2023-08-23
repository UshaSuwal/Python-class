# Class method are the methods which takes class as the first parameter rather than self.
# Classmethod is created using @classmethod decorator
# Static methods are the methods which neither takes class nor self as a parameter.
# They are a normal function which doesn't change the state of the object
# Staticmethod is created using @staticmethod decorator

class Student:
    def __init__(self,age):
        self.age=age
    
    @classmethod
    def current_age(cls,year):
        age=2023-year
        return cls(age)
    
    @staticmethod
    def institution():
        return "Broadway"     # dont use any self or cls. It dont change anything.

s1=Student(25)
print(s1.age)  #25
s2=Student.current_age(1992)
print(s2.age)  # 31
print(s2.institution())  # Broadway