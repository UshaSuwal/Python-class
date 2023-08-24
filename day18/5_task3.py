# Create a function to check whether a input character is vowel or not. 
# Handle the possible exceptions.

def is_vowel(take):
    if any([take.isnumeric(),len(take)>1,type(take)!=str]): 
        return False
    return take.lower() in ['a','e','i','o','u']
t=input("enter a character ")
print(is_vowel(t))

# No any exception

