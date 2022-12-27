# enter your code here
m = input('Please input an integer:')
n = input('Please input an integer:')

lis = []
m = int(m)
n = int(n)
for i in range (m,n+1):
    if i % 3 == 0 and i % 6 != 0:
        lis.append(i)
    if i % 2 == 0 and i % 6 != 0:
        lis.append(i)
print(lis)
