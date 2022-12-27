m = int(input("please input an integer: "))
n = int(input("please input an integer: "))

l = []
for i in range(m, n+1):
    if i>=m:
        if i<=n:
            if i%3 == 0 or i%2 == 0:
                if i%6 != 0:
                    l.append(i)
print(l)
