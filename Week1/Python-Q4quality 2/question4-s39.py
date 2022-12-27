m = input("Please enter an integer: ")
m = int(m)
n = input("Please enter another integer: ")
n = int(n)

sequence_b = []

for i in range(m, n+1):
    if i%3 == 0 or i%2 == 0:
        sequence_b.append(i)

sequence_c = []

for j in sequence_b:   
    if j%6 != 0:
        sequence_c.append(j) 

print(sequence_c)
