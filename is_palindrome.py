import string

def is_palindrome(a):

    # making 2 copies of the string
    # first one is in lowercase and without spaces
    # second one is the reverted version of the first
    
    a1 = a.replace(" ","").lower()
    b = a1[::-1]

    if a1 == b:
        print("YES")
    else:
        print("NO")

# checking if the string matches the required pattern
# and has at least 1 alphanumeric character or space

def validate_raw_string(a):

    # "allowed symbols" is required for checking if any of argument characters do not match the required pattern
    ALLOWED_SYMBOLS = string.ascii_lowercase + " " + string.ascii_uppercase + string.digits

    while len(a) == 0:
        return False
    
    for char in set(a):
        while char not in ALLOWED_SYMBOLS:
            return False
            continue
    else:
        return True
        
a = input("Please enter your string: ")
        
if validate_raw_string(a):
    is_palindrome(a)
else:
    print("A string should contain at least one alphanumeric character and/or space")
