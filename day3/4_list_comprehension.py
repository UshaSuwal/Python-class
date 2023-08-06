# we can loop(for loop) through the list in following way

a=[1,2,3,4]
for i in a:
    print(i)


b=[]
a=[1,2,3,4]
for i in a:
    b.append(i**2)
print(b)
# this is long code and is time consuming SO list comprehension is used


#Using list comprehension for above program:
b=[i**2 for i in a]
print(b)
