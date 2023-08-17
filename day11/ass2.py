#write a python program to calculate difference between a given number and 17. if the number is greater 
#than 17, return twice the absolute difference

n=int(input("enter a number "))
diff=n-17
if diff>0:
    print("twice difference=",diff*2)
else:
    print("difference=",diff)