# enter your code here

m = int(input("Please input the first integer") )
n = int(input("Please input the second integers") )

#n number list
n_list = []
for number in range(n+1):
    n_list.append(number)

#Larger than or equal to m 
critera_list = []
# print(n_list)
for b in n_list:
    if b<m:
        continue
    elif b%3 == 0 or b%2 == 0:
        if b%6 != 0:
            critera_list.append(b)
        
print(critera_list)
