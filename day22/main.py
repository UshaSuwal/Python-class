from create import create_student
from read import read_student
from update import update_student
from delete import delete_student

def inquiry():
    selection=input("Enter your choice c/r/u/d/e ")
    selection=selection.lower()

    def exit_message():
        print("Thankyou. See you again")


    if selection=="c":
        repeat=create_student()    # repeat will have True or False value which is returned from create.
        inquiry() if repeat else exit_message()      
    elif selection=="r":
        student_id=input("Enter the student id ")
        repeat=read_student(student_id)
        inquiry() if repeat else exit_message()
    elif selection=="u":
        student_id=input("Enter the student id ")
        repeat=update_student(student_id)
        inquiry() if repeat else exit_message()
    elif selection=="d":
        student_id=input("Enter a id you want to delete ")
        repeat=delete_student(student_id)
        inquiry() if repeat else exit_message()
    else:
        exit_message()


if __name__=="__main__":
    inquiry()