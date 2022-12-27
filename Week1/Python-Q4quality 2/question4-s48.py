m = int(input("Please input an integer: "))
n = int(input("Please input an integer: "))

values = []

between = m-1

for i in range(m,n+1):
    between += 1
    if between%6!=0:
        if between%3 ==0:
            values += [between]
        elif between%2==0:
            values += [between]
print(values)
