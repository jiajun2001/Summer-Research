# %%
"""
# COMP SCI 2009 Programming for IT - W11 - Practical
"""

# %%
"""
# Set Covering
As mentioned in the lecture, the **set cover problem** is an NP-complete problem. In this task, you will solve this question using both exhausive search (brute force) and greedy apporach. 

The problem is defined as follow:

Given a `list` of `sets` where each `set` contains integers, please find the minimum number of sets that cover the integers from `1` to `10`

For example, given the following three sets:
1. `[1, 2, 3, 4, 5]`
1. `[2, 4, 6, 8]`
1. `[6, 7, 8, 9, 10]`

Your code should find that `set1` and `set3` will cover all the integers from `1` to `10`.

"""

# %%
"""
## Exercise 1: Set cover - brute force 

First, implement the brute force approach that tests `all` combinations. You can assume there will be a solution. To simplify your code a bit, you can use the `itertools`. Please read its document and examples below:

- https://www.geeksforgeeks.org/itertools-combinations-module-python-print-possible-combinations/
- https://docs.python.org/3/library/itertools.html
"""

# %%
import itertools

def brute_force_set(li):
    # INSERT YOUR CODE BELOW
    # use itertools.combinations
    # ~ 8 lines
    for i in range(len(li)+1): #setting up the ramping up of itertools.combinations()
        for cmb in itertools.combinations(li, i): #look for all the possible combinations
            flat = tuple(itertools.chain.from_iterable(cmb)) #flatten the tuple
            if len(flat) == 10: #if the list contain 10 elements
                if len(set(flat)) == len(flat): #check the length of a set() is equal to original len() of the list
                    return cmb #equals, we got it
                

# ================
# TEST CASES BELOW

set_list1 = [ # first test input
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9, 10],
    [1, 3, 7],
    [2, 4, 6, 8]
]

set_list2 = [ # second test input
    [4, 2, 5],
    [1, 7],
    [2, 4, 8, 9, 10],
    [5, 10],
    [3, 5, 6],
    [2, 6],
    [1, 8, 9, 10]
]
            
ss = brute_force_set(set_list1)
print(ss) # ([1, 2, 3], [4, 5, 6], [7, 8, 9, 10])
print('---')
ss = brute_force_set(set_list2)
print(ss) # ([1, 7], [2, 4, 8, 9, 10], [3, 5, 6])


# %%
"""
## Exercise 2: Set cover - greedy



In this exercise, please implement a greedy algorithm that **for each step, takes a set that contains the most uncovered integers** until it covers all integers from `1` to `10`.
"""

# %%
import copy
def greedy_set(list_sets):
    sets = list_sets.copy()
    ans = [] # your answer, should be a list of sets
    covered = {}
    
    #to find the list with most items
    tmp=[]
    for i in sets:
        tmp.append(len(i)) #add the len of each list into tmp list

    kk = 0
    while True:
        # INSERT YOUR CODE BELOW
        # Step 1: search for the set with most uncovered integers
        # Step 2: add the set into ans
        # Step 3: check if ans already cover all integers
        # ~ 15 lines
        for n in range(len(sets)): #set up for the search
            x = tmp.index(max(tmp)) #find the index of list with max items
            in_dict = [k for k in sets[x] if k in covered] #see if the elements of the list is in dictionary
            if len(in_dict) != 0: #if there are items in dict already
                tmp[x] = 0 #set the location of the list to 0, so it won't be picked again
                break #break the for loop, to next iteration 
            else: #if ALL the items in the list is not in dict
                for j in sets[x]: 
                    covered[j] = 1 #add the items into dict
                ans.append(sets[x]) #add the list to ans
                tmp[x] = 0 #clear the value of the list, so we won't revisit it again
        if len(covered) == 10: #if len of dict is 10, that means we found what we want
            return ans #returning the list

        
        # BELOW 3 LINES ARE TO AVOID INFINITE LOOP FOR YOU
        kk += 1
        if kk > 10:
            break

# ================
# TEST CASES BELOW

set_list1 = [ # first test input
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9, 10],
    [1, 3, 7],
    [2, 4, 6, 8]
]

set_list2 = [ # second test input
    [4, 2, 5],
    [1, 7],
    [2, 4, 8, 9, 10],
    [5, 10],
    [3, 5, 6],
    [2, 6],
    [1, 8, 9, 10]
]

s = greedy_set(set_list1)
print(s) # [[7, 8, 9, 10], [1, 2, 3], [4, 5, 6]]
print('---')
s = greedy_set(set_list2)
print(s) # [[2, 4, 8, 9, 10], [3, 5, 6], [1, 7]]

# %%
"""
# Exercise 3 - Knapsack Problem

It’s Boxing Day and you are in a shopping contest! You have one shopping bag and you would like to fill your bags with items that have the largest sum of values. Please solve this problem using dynamic programming.
"""

# %%
bag1 = 4 # the maximum weight for the bag
item_list1 = [
    ['guitar', 4, 3000],
    ['speaker', 1, 1500],
    ['laptop', 3, 2000]
]

bag2 = 7 # the maximum weight for the bag
item_list2 = [
    ['pasta', 1, 700],
    ['soups', 3, 300],
    ['pork', 3, 700],
    ['steak', 4, 1000],
    ['lamb', 3, 1200],
    ['Cheese', 1, 900],
    ['Mushroom', 1, 800],
]

def knapsack_dp(bag_size, items):
    num_row = len(items)
    num_col = bag_size    
    grid = [[0]* (num_col+1) for _ in range(num_row)] # initialise the grid    
    prev_max = 0
    
    # INSERT YOUR CODE
    # Update the DP table (the variable grid)
    # ~ 15 lines
    for i in range(num_row):
        for j in range(num_col+1):
            if j != 0: #not the first column
                if i == 0: #if it is the first row
                    if items[i][1] <= j: #compare the "slots", if the first item can fit
                        grid[i][j] = items[i][2] #put the item (value) in
                else: #not the first row
                    if items[i][1] > j: # if the item cannot fit
                        grid[i][j] = grid[i-1][j] #copy the highest valued option from last row
                    else: #if the item can fit
                        if (items[i][2] + grid[i-1][j-items[i][1]]) > grid[i-1][j]: #compare the combined value of the item and the highest valued compliment option from last row
                            grid[i][j] = items[i][2] + grid[i-1][j-items[i][1]] #if it is greater than the last best option (on last row), update the new combination
                        else: #if the last row have a better option
                            grid[i][j] = grid[i-1][j] #copy the last best option
    return grid

def display(grid):
    for r in grid:
        s = ' '
        for c in r:
            s += f'{c:4} '
        print(s)

g = knapsack_dp(bag1, item_list1)
display(g)
print('---')
g = knapsack_dp(bag2, item_list2)
display(g)

# output should be as below

#     0    0    0    0 3000 
#     0 1500 1500 1500 3000 
#     0 1500 1500 2000 3500 
# ---
#     0  700  700  700  700  700  700  700 
#     0  700  700  700 1000 1000 1000 1000 
#     0  700  700  700 1400 1400 1400 1700 
#     0  700  700  700 1400 1700 1700 1700 
#     0  700  700 1200 1900 1900 1900 2600 
#     0  900 1600 1600 2100 2800 2800 2800 
#     0  900 1700 2400 2400 2900 3600 3600 

# %%
