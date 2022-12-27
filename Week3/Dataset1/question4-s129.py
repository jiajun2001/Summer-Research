m = int(input('Please input an integer: '))
n = int(input('Please input an integer: '))

li = []
li2 = []
for i in range(m, n+1):
        li.append(i)

for i in li:
    if i >= m and i <=n and (i % 3 == 0 or i % 2 == 0) and i % 6 != 0:
        li2.append(i)
        
print(li2)
