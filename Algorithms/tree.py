import pprint
import unittest 
from stack import Stack 

'''Tree with depth first and breadth first traversal algorithms

Each node may have several children. 

1: deal with the node and then with all children (with all subtrees) (breadth-first search or BFS)
2: deal with all children and finally with the node (depth-first search of DFS)  


The traversal algorithms are implemented as separate functions, 
following a simple visitor pattern. 

The advantage of this pattern are the following: 

- by changing the node class (e.g. subclassing and overloading the visit function), 
a user can decide on what to do when a node is visited. 
See for example NodeSquared

- by providing additional visitors, the user can change the order of the graph
traversal, or change the implementation of a given graph traversal algorithm 
for better performance. In this module, there are several implementations.


'''


class Node(object):
    '''
    Implements a tree: 
    each node has an arbitray number of children 
    '''
    
    def __init__(self, value):
        '''constructor. 
        value can be anything, even a complex object. 
        '''
        self.value = value   # wrapped object
        self.children = []
        self.visited = False
        # not necessary for standard visitors, and inelegant.
        # indeed,  it is good to able to call another visitor on the same nodes
        # without having to re-initialize the nodes.

    def visit(self):
        return self.value

    def set_children(self, children):
        '''set the children'''
        self.children = children


    def __repr__(self):
        '''unique string representation'''
        
        return str('node: {val} {children}'.format(
            val = self.value,
            children=self.children
            ) )

class NodeSquared(Node):
    def visit(self):
        return self.value**2

    
def bfs_recursive(nodes, result):
    '''Breadth first recursive implementation
    each recursion is one level down the tree'''
    childnodes=[]
    if len(nodes) is 0:
        return 
    for node in nodes:
        result.append( node.visit() )
    for node in nodes:
        childnodes.extend(node.children)
    bfs_recursive(childnodes, result)
        


def bfs_iterative(nodes, result):
    '''Breadth first iterative implementation
       '''    
    childnodes=[]
    while len(nodes):
        for node in nodes:
            result.append( node.visit() )
        for node in nodes:
            childnodes.extend(node.children)
        nodes=childnodes
        childnodes=[]

    
def dfs_recursive(root, result):
    '''depth first search recursive implementation
    '''
    if root is None:
        return 
    result.append( root.visit() )
    for node in root.children:
        dfs_recursive(node, result)
        

def dfs_iterative(root, result):
    '''depth first search iterative implementation
        in same order as for recursion'''    
    todo = Stack()
    todo.append(root)
    while len(todo):
        node = todo.pop()
        result.append(node.visit())
        for node in reversed(node.children): #reversal makes it match dfs_recursive
            todo.append(node)
        

def dfs_iterative_2(root, result):
    '''depth first search iterative implementation
        children are traversed in a different order to previous algorithms (but its more efficient)''' 
    todo = Stack()
    todo.append(root)
    while len(todo):
        node = todo.pop()
        result.append(node.visit())
        for node in node.children:
            todo.append(node)
        



class TreeTestCase( unittest.TestCase ):

    def setUp(self):
        '''
        called before every test. 
        0 = is the head node

              4  
             /  
            /  
           1--5--7
          / \
         /   \
        0--2  6
         \
          \
           3
        '''
        # building all nodes
        self.nodes = dict( (i, Node(i) ) for i in range(8) )
        # setting children. note that each node keeps track of its children,
        # no need for the polytree class
        self.nodes[0].set_children( [self.nodes[1], self.nodes[2], self.nodes[3] ])
        self.nodes[1].set_children( [self.nodes[4], self.nodes[5] ,self.nodes[6]])
        self.nodes[5].set_children([self.nodes[7]])
        
        # decide on a root for the tests
        self.root = self.nodes[0]

    def test_bfs_recursive(self):
        result = []
        bfs_recursive( [self.root], result )
        # the result is equal to [0, 1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(result, range(8) )

    def test_bfs_iterative(self):
        result = []
        bfs_iterative( [self.root], result )
        # the result is equal to [0, 1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(result, range(8) )

    def test_dfs_recursive(self):
        result = []
        dfs_recursive( self.root, result )
        # the result is equal to [0, 1, 4, 5, 7, 6, 2, 3]
        self.assertEqual(result, [0, 1, 4, 5, 7, 6, 2, 3])
   
    def test_dfs_iterative(self):        
        result = []
        dfs_iterative( self.root, result )
        # the result is equal to [0, 1, 4, 5, 7, 6, 2, 3]
        self.assertEqual(result, [0, 1, 4, 5, 7, 6, 2, 3])
        
    def test_dfs_iterative_2(self):        
        result = []
        dfs_iterative_2( self.root, result )
        # the result is equal to [0, 3, 2, 1, 6, 5, 7, 4] #for this algoritm more "natural" to do children "backwards"
        self.assertEqual(result, [0, 3, 2, 1, 6, 5, 7, 4])

if __name__ == '__main__':
    unittest.main()
