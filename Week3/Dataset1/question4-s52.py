# enter your code here
m = input('Input your integer here: ')
m = int(m)
n = input('Input your second integer here: ')
n = int(n)

list_2 = []

for i in range(m,n+1):
    if i >= m and i <= n:
        if i%3 == 0 or i%2 == 0:
            if i%6 != 0:
                list_2.append(i)
print(list_2)
