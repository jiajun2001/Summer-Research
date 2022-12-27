# enter your code here
m = int(input('Please input an integer for m: '))
n = int(input('Please input an integer for n: '))

#create empty list
li_c = []
#use for loop to every number in the range of m to n
for i in range(m,n+1):
    #check if i meets the criteria
    if (i%3==0 or i%2==0):
        if (i%6!=0):
            li_c.append(i)#if criteria is met add to the empty list
print (li_c)
