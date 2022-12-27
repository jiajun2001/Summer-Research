# enter your code here
print('Please input an integer:')
m = int(input())
print('Please input an integer:')
n = int(input())

# enter your code here
L = []
for i in range(m, n+1):
    if i%3==0 or i%2==0:
        if i%6!=0:
            L.append(i)
print(L)
