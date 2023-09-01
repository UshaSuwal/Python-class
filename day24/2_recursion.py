# If a function is called from the definition of the same function then it is called as a recursive function.

c=0
def count():
    global c
    print(c)
    if c==10:
        return c
    c+=1
    count()
print("sum=",count())