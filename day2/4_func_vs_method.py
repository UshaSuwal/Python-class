
#FUNCTION
def addition(a,b):
    return a+b
print(addition(2,3))




#METHOD
class student:
    def age_after_10_years(self,current_age):
        return current_age+10
s=student()   #s is object
age=s.age_after_10_years(10)
print(age)