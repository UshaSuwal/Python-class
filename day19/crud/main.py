#from crud.create import create_student
#from crud.read import read_student
#from day19.crud.update import update_student
#from day19.crud.delete import delete_student

import json
filename="student_info.json"

## create
def create_student():
    id=input("Enter student id")
    name=input("Enter student name")
    age=input("enter student age ")

    student=dict(id=id,name=name,age=age)
    with open(filename,"w") as fp:
        data=json.dumps(student)
        fp.write(data)
    print("Student Added Successfully")




def inquiry():
    selection=input("Enter your choice c/r/u/d/e")
    selection=selection.lower()

    def exit_message():
        print("Thankyou. See you again")


    if selection=="c":
        create_student()
    elif selection=="r":
        read_student()
    elif selection=="u":
        update_student()
    elif selection=="d":
        delete_student()
    else:
        exit_message()


if __name__=="__main__":
    inquiry()