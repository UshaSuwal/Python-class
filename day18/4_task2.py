# Create a dictionary student with keys id, name, age, department. 
# Take a input from the user, which info (id, name, age or department) 
# he wants to access and print the result. Handle the possible exceptions.
student={"id":7,"name":"john","age":30,"department":"abc"}
try:
    take=input("enter a key (id,name,age,department)")
    info=student[take]
except KeyError:
    print("Please enter valid key")
else:
    print(f"info is ",info)



# Note:
# psql -U postgres
# in mac: postgres
# C:\Program Files\PostgreSQL\15\data
#postgress1212