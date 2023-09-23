# write a python function that accepts a string & calculate number of upper case letters & lower case letters
# sample string : "The quick Brow Fox"
# expected output : no.of upper case letters : 3, no.of lower case letters : 12

string = input("enter a string :")
count1 = 0
count2 = 0
for i in string:
    if(i.islower()):
        count1=count1+1
    elif(i.isupper()):
        count2=count2+1
print("the no.of lower case letters :")
print(count1)
print("the no.of upper case letters :")
print(count2)