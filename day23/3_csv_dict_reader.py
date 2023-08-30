import csv

filename="students.csv"
result=[]
with open(filename,"r") as cr:    #cr=csv reader
    csv_reader=csv.DictReader(cr)
    for each in csv_reader:
        print(each)
        result.append(each)
print(result)

# Output:
#{'id': '1', 'name': 'John', 'age': '30', 'address': 'ktm'}
#{'id': '2', 'name': 'Jane', 'age': '45', 'address': 'pkr'}
#{'id': '3', 'name': 'Ken', 'age': '21', 'address': 'bkt'}

#[{'id': '1', 'name': 'John', 'age': '30', 'address': 'ktm'}, 
# {'id': '2', 'name': 'Jane', 'age': '45', 'address': 'pkr'}, 
# {'id': '3', 'name': 'Ken', 'age': '21', 'address': 'bkt'}]