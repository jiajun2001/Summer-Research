# %%
"""
# W03 Prac - Hash
"""

# %%
"""
# Exercise 1 - Hash Functions

In this weekâ€™s workshop, you have analysed different types of hash functions. Now, please implement and evaluate these hash functions. 

Please implement the following hash functions where `val` is the input and `n` is the size of the hash table. You can assume that the `val`  will be a lower-case string.
1. `hash1(val, n)` : return â€˜1â€™ for all input
1. `hash2(val, n)` : Use the length of the string as the index
1. `hash3(val, n)` : Use the first character as the index
1. `hash4(val, n)` : Map every letter to a prime number, e.g. a = 1, b = 2, c = 3, d = 5â€¦. For a string, the hash function is the sum of all the corresponding numbers modulo the size of the hash. For example, if the hash table is 10, and the string is â€˜badâ€™, the index is `(3+2+7)%10 = 2`. Note that you should ignore the characters that is not in the prime number mapping below.
"""

# %%
def hash1(val, n):
    print("1")
    return 1

def hash2(val, n):
    print(len(val))
    return(len(val))

def hash3(val, n):
    d = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
    list = d
    print (list[val[0]])
    return list[val[0]]

def hash4(val, n):
    d = {'a': 1, 'b': 2, 'c': 3, 'd': 5, 'e': 7, 'f': 11, 'g': 13, 'h': 17, 'i': 19, 'j': 23, 'k': 29, 'l': 31, 'm': 37, 'n': 41, 'o': 43, 'p': 47, 'q': 53, 'r': 59, 's': 61, 't': 67, 'u': 71, 'v': 73, 'w': 79, 'x': 83, 'y': 89, 'z': 97}    
    ...
    
# TEST CASES BELOW
hash1('adelaide', 10) # 1
hash2('adelaide', 10) # 8
hash3('adelaide', 10) # 0
hash4('adelaide', 10) # 6    

# %%
"""
# Exercise 2 - Hash Table 
"""

# %%
"""
In this exercise, you will implement your own HashTable class. You will use chaining when collisions happen. The functions to be completed are
- `add_element(self, val)` function inserts an element into the hash table. Your code should first calculate the hash number of the input value `val`, then insert it into the table.
- `search(self, val)` function search for the input value `val` in the hash table. If the value is already inside the table, it should return `True`, otherwise `False`.

The provided test code first reads a list of books from a file `books.txt`, and then constructs a HashTable containing all books. You can think of it as a book management system in a library that keeps track of weather a book is inside the library.
"""

# %%
size = 0
table = []
collision = 0

def create_table(table_size):
    global size, table, collision
    size = table_size
    table = [[] for i in range(table_size)] # allocate an empty 2D list
    collision = 0 # number of collision

def add_element(val):
    #'''add an element into the hash table'''
    # insert the book name into the hash table, and 
    # if collision happens, increase the value by 1
    # ~ 4 lines of code
    # INSERT YOUR CODE BELOW
    ...
        
def search(val):
    #'''search if the val is already in the hash table'''
    # ~ 5 lines of code
    # INSERT YOUR CODE BELOW
    ...
        
def hash4_b(val):
    d = {'a': 1, 'b': 2, 'c': 3, 'd': 5, 'e': 7, 'f': 11, 'g': 13, 'h': 17, 'i': 19, 'j': 23, 'k': 29, 'l': 31, 'm': 37, 'n': 41, 'o': 43, 'p': 47, 'q': 53, 'r': 59, 's': 61, 't': 67, 'u': 71, 'v': 73, 'w': 79, 'x': 83, 'y': 89, 'z': 97}
    # Copy your hash4 function to here
    # Note that you will need to handle exception 
    # i.e if the character does not have a primary mapping, map it to 0
    # ~8 lines
    # INSERT YOUR CODE BELOW
    ...
# ----------------
# TEST CODE BELOW
with open('books.txt', 'r') as f:
    create_table(10)
    for line in f:
        line = line.strip()
        add_element(line)
print(f'Number of collision is {collision}') # should be 90
print(search('a clockwork orange'))          # should return True
print(search('1984'))                        # should return True
print(search('game of throne'))              # should return False
print(search('foundation'))                  # should return False

with open('books.txt', 'r') as f:
    create_table(100)
    for line in f:
        line = line.strip()
        add_element(line)
print(f'Number of collision is {collision}') # should be 34

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
    nums = li
    if len(set(nums)) == len(nums):
        return False
    else:
        return True

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
    ...
# ---------------            
# TEST CASE BELOW
ans = two_sum([2, 7, 11, 15], 22)
print(ans) #(3, 1)
ans = two_sum([2, 7, 11, 15], 18)
print(ans) #(2, 1)
ans = two_sum([2, 7, 11, 15], 10)
print(ans) #None