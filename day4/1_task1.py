# create a list of first  10 multiple of 3 using list comprehension


b=[]
for i in range(1,11):
    b.append(i*3)
print(b)


#using  list comprehension
b=[i*3 for i in range(1,11)]
print(b)