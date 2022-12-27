# enter your code here
m = int(input ("m: "))
n = int(input ("n: "))

list_Q4 = []
for i in range(m,n+1):
    if i % 3 == 0 and i % 6 !=0:
        list_Q4.append(i)
    if i % 2 == 0 and i % 6 != 0:
        list_Q4.append(i)
print(list_Q4)
