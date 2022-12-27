# enter your code here
m = int(input('Please input an integer: '))
n = int(input('Please input an integer: '))

# for loop
li3 = []

for i in range(m,n+1): # range - larger than or euqal to m and smaller than n
    if i % 2 == 0 or i % 3 == 0: # add all numbers can divisible by 2 or 3
        li3.append(i)
    if i % 6 == 0: # remove the numbers can not divisible by 6
        li3.remove(i)

print(li3)
