# We can open, close, read, write or perform any other kind of work with file using Python
# There are several modes from which we can open a file

# r => read file
# w => write in file           , overwrite hunxa     
# a => append mode
# r+ => read and write mode     ,append jasto hunxa
# w+ => write and read mode     , overwrite gardinxa
# x => exclusive write mode     , if file already exits then it raise error
# a+ => append and read mode



filename="message.txt"
fp=open(filename,"w")
fp.write("hello world")
fp.close()


fp=open(filename,"r")
data=fp.read()
print(data)
print(type(data)) # String    # file bata read gareko data is always string.
fp.close()

# Closing the file is important as it protects the system from memory leakage.
# But sometime we may forget to close the file
# so it is better to open file with context manager

# Context Manager
with open(filename,"a") as fp:     # file close garirakhnu parena yesma chai
    fp.write("\nI'm learning Python")

with open(filename,"r+") as fp:
    data=fp.read()
    print(data)
    fp.write("Python is a high level language")  

with open(filename,"r+") as fp:
    data=fp.read()
    print(data)
    fp.seek(0)  # it puts the filw pointer(cursor) to the start of the file
    fp.write("Python is a high level language")  

with open(filename,"w+") as fp:
    fp.write("This is me who is learning")    #overwrite gardinxa
    fp.seek(0)
    data=fp.read()
    print(data)  

# with open(filename,"x") as fp:
   # fp.write("Hello World.I'm learning python")
# filename= message.txt is already created so it will raise error
