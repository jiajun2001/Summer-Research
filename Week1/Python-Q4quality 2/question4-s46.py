# enter your code here
m = int(input("Please input an integer: "))
n = int(input("Please input an integer: "))

new_num_list = []
for num in range(m, n+1):
    if num % 6 != 0:
        if num % 2 == 0 or num % 3 == 0 :
            new_num_list.append(num)
    
print(new_num_list)

