# enter your code here
m = int(input(f'Please input an integer:'))
n = int(input(f'Please input an integer:'))

li_4=[]
for i in range(m,n+1):#large than r equal to m, smaller or equal than n
    if i%3==0 or i%2==0:#Divisible by 3 or divisible by 2
        li_4.append(i)
    if i%6==0:
        li_4.remove(i)#Not divisible by 6
print(li_4)
