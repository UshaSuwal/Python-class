# Set in python are mutable datatype. However, every element of a set must be immutable.
# Set doesn't support indexing and slicing.
# Set element are always unique.
# Set are unordered.  {1,2} and {2,1} are same.


# Creating an empty set.
a=set()
#a={}. this is not an empty set.It's an empty dictionary.

# Creating non empty set
data={1,2,3,4}
fruits={"apple","banana"}
a={'a',2,3,(1,2),2.5}
print(a)
#b={[1,2],3}  This is not valid set. it raises error because list is mutable.