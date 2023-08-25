# JSON stands for JavaScript Object Notation
# JSON is a file format with .json extention which is used to share data and information over the internet.
# file transfer, info sharing internet ma garnu parda use garinxa

# Python has built-in module for json handling
# JSON is similar to python dictionary as it also written in key-value format.
# But keys and values in JSON data must be enclosed in double-quotes(" "). 
# Single quote are not allowed.
# Integer and float values do not require quotes in JSON

# Some examples of JSON data
{"name":"Harry","age":30,"address":"KTM"}  # Valid JSON
{'name':'Harry','age':30,'address':'KTM'}  # Invalid JSON

[
    {"name":"Harry","age":30,"address":"KTM"},
    {"name":"John","age":22,"address":"BKT"}
]   # Valid JSON  in array

# backend bata data tanda JSON bata taninxa


import json
filename="student.json"
student={'name':'Harry',"age":30,"address":"KTM"}
student1=[
    {"name":"Harry","age":30,"address":"KTM"},
    {"name":"John","age":22,"address":"BKT"}
]

with open(filename,"w") as fp:
    data=json.dumps(student1,indent=2)
    fp.write(data)

with open(filename,"w+") as fp:
    data=json.dumps(student1,indent=2)
    fp.write(data)
    fp.seek(0)
    data=json.loads(fp.read())   #load navako vaye string hunthyo. so traverse garna easy hos vanera list banauxa load le
    print(data)
name=data[0]["name"]   # name= Harry   
name=data[1]["name"]   # name= John
