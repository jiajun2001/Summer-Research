im = int(input('Please input a integer: '))
n = int(input('Please input another integer: '))

print(f'{m}, {n}')
num_match_criteria = []

for i in range(m,(n+1)):
    if (i%3==0 or i%2==0) and (i%6!=0):
        num_match_criteria.append(i)
print(num_match_criteria)
