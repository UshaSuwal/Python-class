from main import session, Student

# reading all data at once
results=session.query(Student).all() # Show all element of table in form of list
print(results)  #[obj1,obj2,obj3]
s1=results[1]
print(s1.name)
print(s1.age)
for student in results:
    print(student.name)
    print(student.age)


# Filtering particular data from the table
student=list(session.query(Student).filter(Student.id==2))
print(student)    # euta purai row  [student object] aauxa
student=student[0]
print(student.name)
print(student.age)


# Updating a data in a row
session.query(Student).filter(Student.id==3).update({"name":"Ken"})  #ORM
session.commit()


# Deleting a row in the table
session.query(Student).filter(Student.id==3).delete()  #ORM
session.commit()
print("A row has been deleted")