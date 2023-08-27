
import json
filename="student_info.json"

def read_student(student_id):
    with open(filename,"r") as fp:
        students=json.loads(fp.read())
    s=list(filter(lambda x:x["id"]==student_id ,students))
    if s:      
        s=s[0]               
        print(s)
    else:
        print("No student of this id")
    repeat=input("Do you want to continue? (Y/N)")
    return True if repeat.lower()=='y' else False


                

        

            
            
