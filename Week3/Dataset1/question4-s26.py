m = int(input('Please enter an integer for m: '))
n = int(input('Please enter an integer for n: '))

mn_condition_list = []

for i in range(m,n+1):
    if i>=m and i<=n:
        if i%2 == 0 or i%3 == 0:
            if i%6 != 0:
                mn_condition_list.append(i)

print(mn_condition_list)
