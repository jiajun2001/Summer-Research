# %%
"""
# W04 Prac
## COMPSCI 2009 Programming for IT
"""

# %%
"""
<!-- BEGIN QUESTION -->

# Exercise 1 - Unweighted DAG
"""

# %%
"""
Please read the code carefully and play with it. After you understand the code, please do the following two things:

### Build an unweighted graph (1pt)

Please use the `add_node` and `add_edge` functions to build a graph below.

![Picture 1.jpg](attachment:ca5546c9-b304-406c-a614-1594d6f9461a.jpg)

### Bredth-first search (1pt)

Please complete the `bfs` function.

"""

# %%
import copy

dag = {} # DAG

def q1_add_node(node, graph):
    # '''add a node into the graph'''
    node = node.lower()
    if node not in graph:
        graph[node] = []
    
def q1_add_edge(node1, node2, graph):
    # '''add an edge from node 1 to node 2'''
    node1 = node1.lower()
    node2 = node2.lower()
    
    # add nodes into graph
    q1_add_node(node1, graph)
    q1_add_node(node2, graph)
    
    # add edge node1 -> node2
    node = graph[node1]
    if node2 not in node:
        node.append(node2)
    
def q1_get_neighbor(node, graph):
    #'''get neighboring nodes'''
    node = node.lower()
    
    if node in graph:
        return copy.deepcopy(graph[node])
    
def q1_show(graph):
    return str(graph)
    
def q1_build_graph(graph):
    # INSERT YOUR CODE BELOW
    # ~ 7 lines
    #q1_add_edge
    q1_add_edge('you', 'alice', graph)#you to alice
    q1_add_edge('you', 'bob', graph) #you to bob
    q1_add_edge('you', 'claire', graph) #you to claire
    q1_add_edge('alice', 'danna', graph) #alice to danna
    q1_add_edge('bob', 'ed', graph) #bob to ed
    q1_add_edge('bob', 'danna', graph) #bob to danna
    q1_add_edge('claire', 'fiona', graph) #claire to fiona
    q1_add_edge('claire', 'george', graph) #claire to george
    # END OF YOUR CODE
    
def q1_bfs(node1, node2, graph):
    #'''return True if there is a path between node1 and node2'''
    node1 = node1.lower()
    node2 = node2.lower()

    # INSERT YOUR CODE BELOW
    # ~ 8 lines
    visited = []
    to_visit = [node1] #nodes to visit
    current = []
    visited = q1_get_neighbor(node1, graph) #visited now has the neighbor of node1 (which is node2) and graph, 2 args of q1_get_neighbor
    while to_visit: #while looking into to_visit
        current = to_visit.pop(0) #pops first element of to_visit into current
        if current not in visited:
            visited.append(current) #appends current to visited
        to_visit.extend(q1_get_neighbor(current, graph)) #.extend essentially appends an entire list into another list; appends the neighbors of current into to_visit
        if node2 == current: #if node2 is the current node, return true
            return True
    return False    

# TEST CASE FOR FIRST TASK BELOW
q1_build_graph(dag)
print(q1_show(dag))  # output: {'you': ['alice', 'bob', 'claire'], 'alice': ['danna'], 
                  # 'bob': ['ed', 'danna'], 'claire': ['fiona', 'george'], 
                  # 'danna': [], 'ed': [], 'fiona': [], 'george': []}

# TEST CASE FOR SECOND TASK BELOW
f = q1_bfs('you', 'fiona', dag)
print(f) # True
f = q1_bfs('alice', 'bob', dag)
print(f) # False

# %%
"""
<!-- END QUESTION -->

# Exercise 2 - Weighted DAG
"""

# %%
"""
Below is another weighted graph `MyWDAG`. Please read the code carefully and play with it. After you understand the code, please do the following two things:

### Build a weighted graph (1pt)

Please use the `add_node` and `add_edge` functions to build a graph below.

![Picture 2.jpg](attachment:78cd9b39-7083-41ef-8834-3a135c5fb5b6.jpg)

### Implement Dijkstra (1pt)

Please complete the `dijkstra()` function above and use the code below to test it.
"""

# %%
import copy

mywdag = {} # MyWDAG

def q2_add_edge(node1, node2, graph, weight = 1):
    # '''add an edge from node 1 to node 2'''
    node1 = node1.lower()
    node2 = node2.lower()

    if not node1 in graph:
        graph[node1] = {}
    if not node2 in graph:
        graph[node2] = {}
    graph[node1][node2] = weight

def q2_get_neighbor(node, graph):
    #'''get neighboring nodes'''
    node = node.lower()
    if node in graph:
        return copy.deepcopy(graph[node])

def q2_show(graph):
    return str(graph)

def q2_build_graph(graph):
    # DIJKSTRA TESTING
    # INSERT YOUR CODE BELOW
    # ~8 LINES
    q2_add_edge('a', 'b', graph, weight = 5) #a -> b
    q2_add_edge('a', 'c', graph, weight = 0) #a -> c
    q2_add_edge('b', 'd', graph, weight = 15) #b -> d
    q2_add_edge('b', 'e', graph, weight = 20) #b -> e
    q2_add_edge('c', 'd', graph, weight = 30) #c -> d
    q2_add_edge('c', 'e', graph, weight = 35) #c -> e
    q2_add_edge('d', 'f', graph, weight = 20) #d -> f
    q2_add_edge('e', 'f', graph, weight = 10) #e -> f

def q2_dijkstra(node1, node2, graph):
    node1 = node1.lower()
    node2 = node2.lower()

    max_c = 10000
    costs = {}
    visited = []

    # initialise costs
    for k in graph:
        costs[k] = max_c
        # print(costs)

    # add initial nodes
    nei = graph[node1]
    for n in nei:
        costs[n] = graph[node1][n]

    # dijkstra algorithm start
    while True:
        max_c = 10000
        node = -1

        # Find lowest cost unvisisted node and set it as node
        # ~ 6 lines
        # INSERT YOUR CODE BELOW
        for n in costs:
            newest_cost = costs[n] #newest_cost is costs[n]
            if costs[n] < max_c: #if number of cost is smaller than max cost
                if n not in visited: #if n is not in visited list
                    node = n #node is now n
                    max_c = newest_cost #max cost is now the newest cost

        # if no unvisisted node, break
        if(node == -1): 
            break

        # Main loop that 
        # 1. Updates the weight around the node with lowest cost
        # 2. Update the visisted node
        # ~ 6 lines
        # INSERT YOUR CODE BELOW
        neighbors = graph[node] #create graph
        for j in neighbors: # for j in neighbors.key
            new_cost = costs[node] + neighbors[j] #new cost is now the node cost and the neighbor [j]
            if new_cost < costs[j]:
                costs[j] = new_cost #if new cost is smaller to costs[j], then costs[j] becomes the new cost
        visited.append(node) #append that node to visited
    return str(costs) #return the string of costs

print(q2_show(mywdag))

# TEST CASE BELOW
q2_build_graph(mywdag)
q2_dijkstra('a', 'f', mywdag) #{'a': 10000, 'b': 5, 'c': 0, 'd': 20, 'e': 25, 'f': 35}

# %%
