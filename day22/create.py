from estd_connection import estd_connection



def create_student():
    cursor=estd_connection()
    id=input("Enter student id ")
    name=input("Enter student name ")
    age=input("enter student age ")

    sql=f"""
    INSERT INTO STUDENT(ID,NAME,AGE) VALUES ('{id}','{name}','{age}')
    """
    cursor.execute(sql)
    print("Student added successfully")
    repeat=input("Do you want to continue? (Y/N)")
    return True if repeat.lower()=='y' else False

