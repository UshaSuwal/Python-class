class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_details(self):
        return f"name is {self.name} and age is {self.age} "
d=Person("John",27)
print(d.get_details())