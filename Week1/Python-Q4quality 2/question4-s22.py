# enter your code here
m = int(input(f'Please input an integer: '))
n = int(input(f'Please input an integer: '))
li3 = []

for i in range(m, n+1):
    if i % 6 == 0:
        continue
    elif i % 3 == 0 & i % 2 == 0:
        li3.append(i)
    elif i % 3 == 0:
        li3.append(i)
    elif i % 2 == 0:
        li3.append(i)
    elif i % 6 == 0:
        continue
        
print(li3)
