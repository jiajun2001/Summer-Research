# enter your code here
m=int(input('Please input an integer:'))
n=int(input('Please input an integer:'))

list_q4=[]
for i in list_q3_forloop:
    if i%2==0 or i%3==0:
        list_q4.append(i)
for j in list_q4:
    if j%6==0:
        list_q4.remove(j)
print(list_q4)
