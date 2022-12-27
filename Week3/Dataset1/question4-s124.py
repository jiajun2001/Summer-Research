# enter your code here
m = input('Please input an integer: ')
m = int(m)

n = input('Please input an integer: ')
n = int(n)

var_list = []

for i in range(m,n+1):
    if i >= m:
        if i <= n:
            if(i % 6 != 0):
                if(i % 3 == 0):
                    var_list.append(i)
                elif(i % 2 == 0):
                    var_list.append(i)

print(var_list)
