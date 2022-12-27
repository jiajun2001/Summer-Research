# enter your code here
m = int(input('Please input an integer: '))
n = int(input('Please input an integer: '))

_list = []


for i in range(m,n+1):
    if i >= m and i <= n:
        if i%3 == 0 or i%2 == 0:
            if i %6 != 0: 
                _list.append(i)

print(_list)
