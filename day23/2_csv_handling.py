# CSV stands for comma separated values
# CSV files have extension .csv

import csv 

filename="students.csv"
with open(filename,"r") as cr:     #cr=csv reader
    csv_reader=csv.reader(cr)
    for each_line in csv_reader:
        print(each_line)

# Output:
# ['id', 'name', 'age', 'address']
# ['1', 'John', '30', 'ktm']
# ['2', 'Jane', '45', 'pkr']
# ['3', 'Ken', '21', 'bkt']



with open(filename,"r") as cr:
    csv_reader=csv.reader(cr)
    result=[]
    for count,each_line in enumerate(csv_reader):
        if count==0:
            continue
        data=dict(id=each_line[0],name=each_line[1],age=each_line[2],address=each_line[3])
        result.append(data)
print(result)

# Output:
# [{'id': '1', 'name': 'John', 'age': '30', 'address': 'ktm'}, 
# {'id': '2', 'name': 'Jane', 'age': '45', 'address': 'pkr'}, 
# {'id': '3', 'name': 'Ken', 'age': '21', 'address': 'bkt'}]
