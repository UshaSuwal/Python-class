import json
filename="student_info.json"

def update_student(student_id):
    with open(filename, "r+") as fp:
        students=json.loads(fp.read())
        s=list(filter(lambda x:x["id"]==student_id,students))
        if s:
            s=s[0]
            index=students.index(s)
            key=input("Enter info you want to update ")
            new_value=input("Enter the new value ")
            s[key]=new_value
            students[index]=s
            fp.seek(0)
            fp.write(json.dumps(students, indent=2))
            print(" Updated successfully")
        else:
            print("Invalid id")
    repeat=input("Do you want to continue? (Y/N)")
    return True if repeat.lower()=='y' else False


