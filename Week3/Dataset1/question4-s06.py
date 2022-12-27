m = input('please input an interger:')
n = input('please input an interger:')
m=int(m)
n=int(n)

li=[]
list=[]
for i in range(10,21):
    if i%3==0 or i%2==0:
        li.append(i)
for e in li:
    if e%6!=0:
        list.append(e)
print(list)
