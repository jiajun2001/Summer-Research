m = input("Please input an integer: ")
n = input("Please input an integer: ")
m = int(m)
n = int(n)

# empty list
list_specifics = []

# using m & n from above
for i in range(m, n+1):  
    if i % 6 == 0:
        i = i
    elif i % 3 == 0:
        list_specifics.append(i)
    elif i % 2 == 0:
        list_specifics.append(i)
    else:
        i = i
        
print(list_specifics)
