
# Create a class Circle with an attribute radius. Create two objects of circle c1 and c2. 
# Add the radius of the circles and print the result.
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def total(self,other):
        return self.radius + other.radius
c1=Circle(5)
c2=Circle(10)
result=c1.total(c2)
print(f"the radius of circles = {result}")    


# Using magic method
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def __add__(self,other):
        return self.radius + other.radius
c1=Circle(5)
c2=Circle(10)
result=c1+c2
print(f"the radius of circles = {result}")    



# WAP to compare the size of circle and print the result using magic method
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def __gt__(self,other):
        if self.radius>other.radius:
            return f"circle with radius {self.radius} is bigger"
        else:
            return f"circle with radius {other.radius} is bigger"

c1=Circle(5)
c2=Circle(10)
result=c1>c2
print(result)    
