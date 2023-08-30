filename="message.txt"
#with open(filename,"w") as fp:
#  fp.write("Hello world \nI'm learning python")


# read()
# seek()
# readline()
# readlines()
# tell()
# writelines()
with open(filename,"r") as fp:
    data=fp.read()
    print(data)     # Hello world I'm learning python

    fp.seek(0)      # fp.read() garesi file pointer last ma pugxa so seek(0) gareko. seek(0) changes cursor of file
    data=fp.read(7) # Hello w
    print(data)  

    fp.seek(0)
    data=fp.readline()  # Hello world
    print(data)

    fp.seek(0)
    data=fp.readlines()   # gives result in list.
    print(data)     #['Hello world \n', "I'm learning python"]

data=['Hello world \n', "I'm learning python \n","Python is high level programming language"]
with open(filename,"w") as fp:
    fp.writelines(data)
    
