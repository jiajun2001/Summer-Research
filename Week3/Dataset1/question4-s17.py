# enter your code here
m = int(input('Please input a integer: '))
n = int(input('Please input a integer: '))

l3=[]
for i in range(m,n+1):
    if i % 2 == 0 and i % 3 == 0:
        continue
    elif i % 2 == 0:
        l3.append(i)
    elif i % 3 ==0:
        l3.append(i)
print(l3)
