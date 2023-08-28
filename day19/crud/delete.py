import json
filename="student_info.json"


def delete_student(student_id):
    with open(filename,"r") as fp:
        students=json.loads(fp.read())
    s=list(filter(lambda x:x["id"]==student_id,students))
    if s:
        s=s[0]
        students.remove(s)
        with open(filename,"w") as fp:
            fp.write(json.dumps(students,indent=2))
            print("Deleted successfully")
    else:
        print("Invalid id")
    repeat=input("Do you want to continue? (Y/N)")
    return True if repeat.lower()=='y' else False


# read xuttai and write xuttai gareko because:
# delete garesi list will be small than previous so r+ garda tala ko remaining baki hunxa 
# so write xuttai gareko.write le purai over write gardinxa.
    