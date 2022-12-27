m = int(input('Please input an interger: '))
 n = int(input('Please input an interger: '))

li = []
for e in range(m, n+1):
    li.append(e)  
li2=[]    
for i in li:
    if i%3==0 or i%2==0:
        li2.append(i)
    if i%6==0:
        li2.remove(i)
        
print(li2)
