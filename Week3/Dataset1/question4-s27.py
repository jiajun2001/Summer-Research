# enter your code here
m= int(input(" Please input an integer : "))
n=int(input(" Please input an integer : "))

lis=[]
for j in range(m,n+1):
    if j%3 == 0 or j%2 == 0:
        if j%6!=0:
        
            lis.append(j)
            
print(lis)
