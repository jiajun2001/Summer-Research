# enter your code here
m = int(input("Please input an interger"))
n = int(input("Please input an interger"))
lis = []
for i in range(m,n+1):
    if i%3 == 0 or i%2 == 0:
        if i%6!=0:
            lis.append(i)
print(lis)
