class Department:
    def __init__(self,t1):
        self.t1=t1

    def total_student(self,a):
        return a.t1+self.t1
    
    def __add__(self,a):
        return a.t1+self.t1

    
d1=Department(20)
d2=Department(30)
result=d1.total_student(d2)
print(result) #50

result=d1+d2   # This calls magic method ie __add__
print(result)  #50