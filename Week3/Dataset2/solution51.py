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

def brute_force_set(subsets):
    # INSERT YOUR CODE BELOW
    # use itertools.combinations
    # ~ 8 lines
    for length in range(len(subsets)): #for length in the range of subsets length
        combined = itertools.combinations(subsets, length) #combined is assigned to combinations of subsets and length
        for potential in combined: #potential is a list of lists
            union = [] #create union list/set
            for end in potential: #for end in potential
                union += end #end is added to union and it becomes the 'new' union
            if set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).issubset(set(union)): #if subset has 10 elements
                return potential #return 'potential' subset
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
def greedy_set(subsets):  #define the function with subsets as variable
    
    union = set() #create union list/set
    result = [] #create result list
    covered = set() #create covered set to put elements that algorithm has found so far

    for subset in subsets: #to find the subset in subsets
        union = union.union(subset) #we append the subset into union set by using the .union function

    while covered != union: #while covered is not equal to union
        subset = [] #create another empty list for subset
        for sset in subsets: # for sset in subsets
            if len(set(sset) - covered) > len(set(subset) - covered): #if the length of sset set - covered is greater than length of subset - covered
                subset = sset #subset is now sset
        result.append(subset) #append subset to result
        covered |= set(subset) #covered is now union to subset, which is now a set with |=
    return result #return the result


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
    for x in range(0, num_row):
        for y in range(1, num_col + 1): #first column will be full of 0's, this is normal as this is initial cost/weight
            if x == 0:
                prev_max = 0 #if x is 0 then the previous max is 0
            else:
                prev_max = grid[x - 1][y]
            item_w = items[x][1]
            new_value = items[x][2] + grid[x - 1][y - item_w] # to get the value of the current item and the previous max value of the remaining weight
            if y >= item_w:
                grid[x][y] = max(prev_max, new_value)
            else:
                grid[x][y] = prev_max

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
