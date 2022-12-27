m = int(input("Please input an integer: "))
n = int(input("Please input an integer: "))

L4 = []
for i in range(n-m+1):
    if ((m+i)%3==0 or (m+i)%2==0) and not ((m+i)%6==0):
        L4.append(m+i)
print(L4)
