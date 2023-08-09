# add()
s={1,2,3}
s.add(4)  #it add 4 in set
print(s)


# update()
s={1,2,3}
s.update([4,5,6])
print(s)  #O={1,2,3,4,5,6}


# remove()
s={1,2,3,4,5,6}
s.remove(4)
print(s)  #O={1,2,3,5,6}
#s.remove(8)  it raises error as 8 is not in set s 

# discard()
s={1,2,3,4,5,6}
s.discard(4)
print(s)
s.discard(8)   #it doesn't raise error


#pop()
s={1,2,3,4}
s.pop()
print(s)   #it randomly pops out any one element from the set


# clear()
s.clear()
print(s)  # {} empty set