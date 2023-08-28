from estd_connection import estd_connection

cursor=estd_connection()

id=input("Enter id")
name=input("Enter name")
age=int(input("Enter age"))

sql=f"""
INSERT INTO STUDENT(ID,NAME,AGE) VALUES ('{id}','{name}','{age}')    # only single quote ''
"""
cursor.execute(sql)
print("Student added successfully!!")