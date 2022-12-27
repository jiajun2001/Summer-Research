# enter your code here
m = input("Please input an integer:")
n = input("Please input an integer:")

li = []

for num in range(m, n+1):
    if num%6 != 0 and (num%3 == 0 or num%2 ==0):
        li.append(num)
print(li)
