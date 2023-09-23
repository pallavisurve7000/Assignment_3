# write a python program to reverse a sring 
#sample string: "1234abcd"
#expected output: "dcba4321"

def reverse(string):
    string = string[::-1]
    return string
s = "1234abcd"
print("reversed string is :", end=" ")
print(reverse(s))