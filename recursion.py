# --------- #
# Recursion #
# --------- #

# Recursion
# In your own words, what is Recursion?
    # recursion is calling a function that calls itself in order to make incremental
    # progress and drill down to a terminating base condition

# Why is it necessary to have a Base Case?  
    # a base case provides the terminating condition where the function will
    # recurse to and complete

# Graphs
# What is a Graph?
    # a graph is a data structure that displays cyclical relationships;  nodes are 
    # connected by edges to demonstrate adjacenciesd

# How is a Graph different from a Tree?
    # trees also have nodes, but are acyclical and only 
    # exhibit parent-child relationships

# Give an example of somthing that would be good to model with a Graph.
    # examples of graph networks are flights where the nodes are destination cities
    # and edges are the flight between 2 cities;  another example is social networks 


# Fill in the runtimes for the following actions for the table below:

# Data Structure                Index   Search  Add-R   Add-L   Pop-L   Pop-R
# Python List (Array)           O(1)    O(n)    O(1)     O(n)   O(n)    O(1)  
# Linked List                   O(n)    O(n)    O(1)     O(1)   O(1)    O(n)     
# Doubly-Linked List            O(n)    O(n)    O(1)     O(1)   O(1)    O(1)
# Queue (as Array)              X       X       O(1)    X       O(n)     X
# Queue (as LL or DLL)          X       X       O(1)    X       O(1)     X
# Stack (as Array, LL, or DLL)  X       X       O(1)    X       X       O(1)
# Deque (as DLL)                X       X       O(1)    O(1)    O(1)    O(1)

# Data Structure          Get     Add    Delete  Iterate  Memory
# Dictionary (Hash Map)   O(1)    O(1)    O(1)    O(n)    medium
# Set (Hash Map)          O(1)    O(1)    O(1)    O(n)    medium
# Binary Search Tree      O(log n)O(n)    O(n)    O(1)    a little
# Tree                    O(n)    O(1)    O(1)    O(1)    a little

# Sorting
# Describe in words how the Bubble Sort algorithm works.
    # bubble sort iterates through the list returning the highest number in a list
    # and moves it to the end, bubble sort will continue to iterate through the list
    # bubbling up the next highest number to its respective place until all numbers
    # are sorted
# Describe in words how the Merge Sort algorithm works.
    # merge sort breaks every element in a list into a list of one, and then merges
    # them back together to make a new sorted list
# Describe in words how the Quick Sort algorithm works.
    # quick sort is the divide and conquer strategy, selects a random pivot and 
    # iterates through the list to place lower numbers to the left of the pivot,
    # and higher numbers to the right.  once the pivot is in the right place, 
    # each side repeats the process recursively

# Git Branching
# Give an instance when you would use git branching.
    # Use git branching when you want to maintain a separate environment from master, such as
    # development or testing (vs. production) when implementing a new feature
# What is a pull request?
    # a pull request is a request made to the project owner to pull your proposed new changes
    # and merge into their branch

# 1. Write a function that uses recursion to print each item in a list.
def print_item(my_list, i=0):
    """Prints each item in a list recursively.

        >>> print_item([1, 2, 3])
        1
        2
        3

    """

    if i > 2:
        return

    print my_list[i]
    i+=1
    print_item(my_list, i)
   


# 2. Write a function that uses recursion to print each node in a tree.

def print_all_tree_data(tree):
    """Prints all of the nodes in a tree.


        >>> class Node(object):
        ...     def __init__(self, data):
        ...             self.data=data
        ...             self.children = []
        ...     def add_child(self, obj):
        ...             self.children.append(obj)
        ...
        >>> one = Node(1)
        >>> two = Node(2)
        >>> three = Node(3)
        >>> one.add_child(two)
        >>> one.add_child(three)
        >>> print_all_tree_data(one)
        1
        2
        3

    # """

    print tree.data
    for child in tree.children:
        print_all_tree_data(child)


 
# 3. Write a function that uses recursion to find the length of a list.


def list_length(my_list):
    """Returns the length of list recursively.
        >>> list_length([1, 2, 3, 4])
        4

    """
    if not my_list:
        return 0

    return 1 + list_length(my_list[1:])


# 4. Write a function that uses recursion to count how many nodes are in a tree.

def num_nodes(tree):
    """Counts the number of nodes.

        >>> class Node(object):
        ...     def __init__(self, data):
        ...             self.data=data
        ...             self.children = []
        ...     def add_child(self, obj):
        ...             self.children.append(obj)
        ...
        >>> one = Node(1)
        >>> two = Node(2)
        >>> three = Node(3)
        >>> one.add_child(two)
        >>> one.add_child(three)
        >>> num_nodes(one)
        3
    """

    # if not tree.children:
    #     return 0

    # for child in tree.children:
    #     return 1 + num_nodes(tree.children)

    # if isinstance(tree, dict):
    #     return sum([num_nodes(tree[n]) for n in tree])
    # else:
    #     return 1

 

#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
