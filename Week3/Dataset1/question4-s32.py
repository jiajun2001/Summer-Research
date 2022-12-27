# enter your code here
m = int(input("please intput an interger: "))
n = int(input("please intput an interger: "))

li = []

for x in range(m , n + 1):
    if x%2 == 0 or x%3 == 0:
        if x%6 != 0:
            li.append(x)
    else:
        continue

print(li)
