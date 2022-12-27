# enter your code here
m = input('Please input an integer: ')
m = int(m)

n = input('Please input an integer: ')
n = int(n)

num_list = []

for x in range(m, n+1):
    if x >= m:
        if x <= n:
            if x % 3 == 0 or x % 2 == 0:
                if x % 6 != 0:
                    num_list.append(x)
                    
print(num_list)
