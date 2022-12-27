m = int(input("Please input an integer: "))
n = int(input("Please input an integer: "))

list4 = []
for x in range(m,n+1):
    if(x%3 == 0 or x % 2 == 0): 
        if(x%6==0):
            list4 = list4
        else:
            list4.append(x)
        
print(list4)
