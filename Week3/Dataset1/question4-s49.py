# enter your code here
m = int(input ('Please input first number:'))
n = int(input ('Please input second number:'))

lis = list(range(m, n))
ans = []
for x in lis:
    if x % 3 == 0 or x % 2 == 0:
        if x % 6 == 0:
            nothing = 'nothing'
        else:
            ans.append(x)

print (ans)
