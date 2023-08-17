nums=[3,4,2,2,1,3,3,3]
a=[]
for i in nums:
    if nums.count(i)>1:
        if i not in a:
            a.append(i)
print(a)