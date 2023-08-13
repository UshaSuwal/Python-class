# While loop is another way to loop in python. "while" takes a statement after it and the loop run until
# this statement is truthy. It stops immediately on getting falsy statement.

n=0
while n<=10:
    print(n)
    n+=1
else:
    print("this is executed if the main loop is compeletely iterated")


#while 3:       # 3 is truthy so infinite loop. Use "while True:" instead of 3.
    #print("hello")
