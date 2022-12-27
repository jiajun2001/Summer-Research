# enter your code here
m = int(input("Please input an integer: "))
n = int(input("Please input an integer: "))

list_4 = []
j = m
while (j >= m  and j <= n):
    if ((j % 3 == 0 or j % 2 == 0) and j % 6 != 0):
        list_4.append(j)
    j = j + 1
    
print(list_4)
