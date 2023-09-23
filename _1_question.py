def sumlist(list):
    sum=0
    for i in range(len(list)):
        sum = sum + list[i]
    return sum
list = [8, 2, 3, 0, 7]
print(list)
print("sum of list:",sum(list))



