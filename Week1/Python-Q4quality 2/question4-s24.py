# enter your code here
m = int(input("Please input an integer: "))
n = int(input("Please input an integer: "))
my_list=[]
    

for i in range(m , n + 1):
    if(i >= m and i <= n and (i % 3 == 0 or i % 2 == 0) and i % 6 != 0):
        my_list.append(i)
print(my_list)
