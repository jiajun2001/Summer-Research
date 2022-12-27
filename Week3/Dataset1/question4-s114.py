# input
m = input(f'Please input an integer m: ')
m = int(m)
n = input(f'Please input an integer n: ')
n = int(n)
print(f'The variable m is {m} and n is {n}')

#create list
li_2 = []
for i in range(m, n):
    if i % 3 == 0 or i % 2 == 0:
        if i % 6 != 0:
            li_2.append(i)
print(li_2)
