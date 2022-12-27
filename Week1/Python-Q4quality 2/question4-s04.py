# enter your code here
m = input('Please input an integer: ')
n = input('Please input an integer: ')
m = int(m)
n = int(n)
list = []

for i in range(m,n+1):
    if i >= m and i < n and (i % 3 == 0 or i % 2 == 0) and i % 6 != 0:
        list.append(i)
        print(list)
