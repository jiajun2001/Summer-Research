# enter your code here
m = input('Please input an integer: ')
m = int(m)

n = input('Please input an integer: ')
n = int(n)

list_n3 = []
for x in range(m,n+1):
    if x % 6 != 0:
        if x % 3 == 0:
            list_n3.append(x)
        elif x % 2 == 0:
            list_n3.append(x)
        
print(list_n3)
