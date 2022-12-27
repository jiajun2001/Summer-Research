# enter your code here

m = int(input("Please input an integer: "))
n = int(input("Please input an integer: "))

newlist3 = []
for i in range(m,n+1):
    if (i % 6 !=0) and ((i % 3 == 0) or (i % 2 == 0)): 
        newlist3.append(i)
        
print(newlist3)
