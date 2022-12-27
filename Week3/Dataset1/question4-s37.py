# enter your code here
m=int(input("Please input an integer: "))
n=int(input('Please input another integer: '))

list4=[]
list5=[]
for u in range(m,n+1):
    if u%6==0:
        pass
    elif u%2==0 or u%3==0:
        list4.append(u)
    
print(list4)
