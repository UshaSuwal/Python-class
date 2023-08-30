# list of dictionary to csv

import csv

student=[{'id': '1', 'name': 'John', 'age': '12', 'address': 'bkt'}, 
         {'id': '2', 'name': 'Keny', 'age': '55', 'address': 'pkr'}, 
         {'id': '3', 'name': 'Sen', 'age': '31', 'address': 'bkt'},
         {'id': '4', 'name': 'Hen', 'age': '25', 'address': 'thimi'}]

filename="student_write.csv"
with open(filename,"w") as cw:
    key_name=student[0].keys()   # ["id","name","age","address"]
    csv_writer=csv.DictWriter(cw, fieldnames=key_name)
    csv_writer.writeheader()
    for i in student:
        if i["age"]<="25":
            csv_writer.writerow(i)

