# enter your code here
m = int(input('assign a number into:'))
n = int(input('insert another number: '))

my_list = []
for i in range(m,n+1,1):
    my_list.append(i) 

for i in my_list:
    if i >= m and i <=n and(i%3 == 0 or i%2 ==0)and i%6 !=0 :
        s.append(i)
print(s)


