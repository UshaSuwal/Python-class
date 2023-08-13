squared=[]
# using normal loop
for i in range(1,6):
    squared.append(i**2)
print(squared)

# using List Comprehension:
squared=[i**2 for i in range(1,6)]


# using dictionary comprehension:
squared_dict={k:k**2 for k in range(1,6)}
#output: {1:1,2:4,3:9,4:16,5:25}


# Dictionary comprehension
student_list=[("name","jon"),("age",25),("address","ktm")]

s={k:v for k,v in student_list}
print(s)
            