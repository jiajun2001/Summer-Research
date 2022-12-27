#prompts the user to input the integers and stores them as variables
m = int(input("Please input an integer: "))
n = int(input("Please input another integer: "))

li = []      #initially defines the blank list

for i in range(m, n+1):   #runs a loop for index values of m to n
    if ((i % 2 == 0 or i % 3 == 0) and i % 6 != 0):     #checks if the value i is divisible by (3 OR 2), AND is not divisible by 6
        li.append(i)
print(li)           #print the resulting list
