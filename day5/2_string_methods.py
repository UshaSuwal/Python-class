#1. capitalize()
message="hello world"
print(message.capitalize())  # Hello world   # agadi ko euta matra capital gardinxa

#2. title()
message="hello world hehe"
print(message.title())     # Hello World Title  # harek word ko agadi ko capital gardinxa

#3. upper()
print(message.upper())    # HELLO WORLD HEHE

#4. lower()
print(message.lower())    # hello world hehe

#5. split()
message="hello all. i am learning Python"
result=message.split()  #calling split() without any parameters. it splits with <space> by default
print(result)   #Output: ["hello","all.","i","am","learning","Python"]

result=message.split('o')  #"o dekhesi spilt gardinxa ani "o" hatauxa"
print(result)  #Output:  ["hell","all. i am learning Pyth", "n"]

message="hello,all,i,am,learning,Python"
result=message.split(",")
print(result)


#6. join()
info=["hello","all.","i","am","learning","Python"]
result=" ".join(info)
print(result)      #hello all. i am learining Python
print("info=",info)   # info chai same nai hunxa

info=["hello","all.","i","am","learning","Python"]
result="+".join(info)    #hello+all.+i+am+learining+Python
print(result) 

info=["hello","all.","i","am","learning","Python"]
result=",".join(info)
print(result) 


#info.join(" ")  yesari mildaina it raises error because join() should be called with string object not with list.



#7. find()
m="hello worLd"
print(m.find('w'))    # O=6 'w' kata xa tyo index dinxa
print(m.find('rLd'))  # O=8 'rld' rld start vayeko index matra dinxa.
print(m.find('f'))    # O=-1 -1 means vetena

search_value='Rld'
result=m.lower().find(search_value.lower())
print(result)


#8. replace()
m="hello world"
result=m.replace("hello","hy")
print(result)   #Output= hy world


