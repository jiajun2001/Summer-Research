# enter your code here
m = int(input("Please input an integer: "))
n = int(input("Please input an integer: "))

my_list = []
for i in range(m, n + 1): #Added +1 to n otherwise it will stop at 19 even though n = 20
    if i >= m and i <= n: #Checks if i is greater or equal to m and that i is also smaller or equal to n
        if i % 3 == 0 or i % 2 == 0: #Checks if i is divisible by 3 or that i is divisible by 2
            if not i % 6 == 0: #Checks if i is NOT divisible by 6
                my_list.append(i) #If the above if statements are True, i will be added to my_list
                
print(my_list)
