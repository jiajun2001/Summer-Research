# enter your code here
m = int(input("Please input an integer: "))
n = int(input("Please input an integer: "))
print(f"m is {m}, n is {n}")

Q4List = []
for x in range(m,n+1):
    if (x/6)-int(x/6) != 0:
        if (x/3)-int(x/3) == 0 or (x/2)-int(x/2) == 0:
            Q4List.append(x)
print(Q4List)
