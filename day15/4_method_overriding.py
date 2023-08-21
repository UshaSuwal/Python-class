class Vehicle:
    def __init__(self,color,doors):
        self.color=color
        self.doors=doors
    def get_details(self):
        return f"color is {self.color} and doors is {self.doors}"
    
class Bike(Vehicle):
    def __init__(self,color,doors,milage,company):
        super().__init__(color,doors)
        self.milage=milage
        self.company=company
    def get_details(self):
        print(super().get_details())
        return f"milage is {self.milage} and company is{self.company}"
b=Bike("red",4,45,"ntorq")
print(b.get_details())