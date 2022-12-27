# %%
"""
# W09 Prac - Hash
"""

# %%
"""
# Exercise 1 - Hash Functions

In this week’s workshop, you have analysed different types of hash functions. Now, please implement and evaluate these hash functions. 

Please implement the following hash functions where `val` is the input and `n` is the size of the hash table. You can assume that the `val`  will be a lower-case string.
1. `hash1(val, n)` : return ‘1’ for all input
1. `hash2(val, n)` : Use the length of the string as the index
1. `hash3(val, n)` : Use the first character as the index
1. `hash4(val, n)` : Map every letter to a prime number, e.g. a = 1, b = 2, c = 3, d = 5…. For a string, the hash function is the sum of all the corresponding numbers modulo the size of the hash. For example, if the hash table is 10, and the string is ‘bad’, the index is `(3+2+7)%10 = 2`. Note that you should ignore the characters that is not in the prime number mapping below.
"""

# %%
def hash1(val, n):
    return 1

def hash2(val, n):
    hash = len(val)
    return hash

def hash3(val, n):
    d = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
    hash = d[val[0]]
    return hash
    
def hash4(val, n):
    d = {'a': 1, 'b': 2, 'c': 3, 'd': 5, 'e': 7, 'f': 11, 'g': 13, 'h': 17, 'i': 19, 'j': 23, 'k': 29, 'l': 31, 'm': 37, 'n': 41, 'o': 43, 'p': 47, 'q': 53, 'r': 59, 's': 61, 't': 67, 'u': 71, 'v': 73, 'w': 79, 'x': 83, 'y': 89, 'z': 97}    
    hash = 0
    for i in val:
        hash += d[i]
    hash = hash%10
    return hash
    
# TEST CASES BELOW
print(hash1('adelaide', 10)) # 1
print(hash2('adelaide', 10)) # 8
print(hash3('adelaide', 10)) # 0
print(hash4('adelaide', 10)) # 6    
print(hash4('apple', 10))

# %%
"""
# Exercise 2 - Hash Table 
"""

# %%
"""
In this exercise, you will implement your own HashTable. You will use chaining when collisions happen. The functions to be completed are
- `add_element(val)` function inserts an element into the hash table. Your code should first calculate the hash number of the input value `val`, then insert it into the table.
- `search(val)` function search for the input value `val` in the hash table. If the value is already inside the table, it should return `True`, otherwise `False`.

The provided test code first reads a list of books from a file `books.txt`, and then constructs a HashTable containing all books. You can think of it as a book management system in a library that keeps track of weather a book is inside the library.
"""

# %%
size = None
table = None
collision = None

def create_table(table_size):
    global table, collision
    size = table_size
    table = [[] for i in range(table_size)]# allocate an empty 2D list
    collision = 0 # number of collision

def add_element(val):
    global table, collision
    #'''add an element into the hash table'''
    # insert the book name into the hash table, and 
    # if collision happens, increase the value by 1
    # ~ 4 lines of code
    # INSERT YOUR CODE BELOW
    x = hash4_b(val)
    if len(table[x]) != 0:
        collision += 1
    table[x].append(val)
        
def search(val):
    global table
    #'''search if the val is already in the hash table'''
    # ~ 5 lines of code
    # INSERT YOUR CODE BELOW
    if val in table[hash4_b(val)]:
        return True
    else:
        return False
        
def hash4_b(val):
    d = {'a': 1, 'b': 2, 'c': 3, 'd': 5, 'e': 7, 'f': 11, 'g': 13, 'h': 17, 'i': 19, 'j': 23, 'k': 29, 'l': 31, 'm': 37, 'n': 41, 'o': 43, 'p': 47, 'q': 53, 'r': 59, 's': 61, 't': 67, 'u': 71, 'v': 73, 'w': 79, 'x': 83, 'y': 89, 'z': 97}
    # Copy your hash4 function to here
    # Note that you will need to handle exception 
    # i.e if the character does not have a primary mapping, map it to 0
    # ~7 lines
    # INSERT YOUR CODE BELOW
    hash = 0
    for i in val:
        if i in d:
            hash += d[i]
    hash = hash%10
    return hash
# ----------------
# TEST CODE BELOW
with open('books.txt', 'r') as f:
    create_table(10)
    for line in f:
        line = line.strip()
        add_element(line)
    print(f'Number of collision is {collision}')
    print(search('a clockwork orange')) # should return True
    print(search('1984')) # should return True
    print(search('game of throne')) # should return False
    print(search('foundation')) # should return False

with open('books.txt', 'r') as f:
    create_table(100)
    for line in f:
        line = line.strip()
        add_element(line)
    print(f'Number of collision is {collision}') # should be 90

# %%
"""
# Exercise 3 - Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

### Example 1:

Input: nums = `[1,2,3,1]` <br>
Output: true
### Example 2:

Input: nums = `[1,2,3,4]` <br>
Output: false
### Example 3:

Input: nums = `[1,1,1,3,3,4,3,2,4,2]` <br>
Output: true


"""

# %%
def check_dup(li):
    # Enter your code below
    # ~ 7 lines
    tmp = []
    for i in li:
        if i in tmp:
            return True
        else:
            tmp.append(i)
    return False

# ---------------
# TEST CASE BELOW

b = check_dup([1, 3, 1, 2])
print(b) # True
b = check_dup([1, 2, 3, 4])
print(b) # False
b = check_dup([1,1,1,3,3,4,3,2,4,2])
print(b) # True

# %%
"""
# Exercise 4 - Two Sum
"""

# %%
"""
Given an array of **integers** nums and an **integer** target, return indices of the two numbers such that they add up to target. 

You may assume that each input would have **exactly one solution**, and you may not use the same element twice. You can return the answer in any order.

**Note:** the most intuitive solution is $O(n^2)$ that checks every pair of the numbers. However, you can use hash table to solve the question in linear time! You will get full mark by using either of the approach. 

### Example 1:

Input: nums = `[2,7,11,15]`, target = `9` <br>
Output: `[0,1]` <br>
Explanation: Because `nums[0] + nums[1] == 9`, we return `[0, 1]`.

### Example 2:

Input: nums = `[3,2,4]`, target = `6` <br>
Output: `[1,2]`

### Example 3:

Input: nums = `[3,3]`, target = `6` <br>
Output: `[0,1]`

"""

# %%
def two_sum(li, target):
    # If using dictionary, ~ 9 lines
    # INSERT YOUR CODE BELOW
    if target in idx_tbl:
        return idx_tbl[target]
    else:
        for i in li:
            if (target - i) in li:
                idx_tbl[target] = (li.index((target - i)), li.index(i))
                return idx_tbl[target]

idx_tbl = {}
# ---------------            
# TEST CASE BELOW
ans = two_sum([2, 7, 11, 15], 22)
print(ans) #(3, 1)
ans = two_sum([2, 7, 11, 15], 18)
print(ans) #(2, 1)
ans = two_sum([2, 7, 11, 15], 10)
print(ans) #None