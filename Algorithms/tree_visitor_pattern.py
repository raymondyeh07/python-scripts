import pprint
import unittest 
from stack import Stack 

'''Tree with Depth First and Breadth First traversal algorithms
implemented using a full visitor pattern (allows improved independence
of Node from algorithm)

Each node may have several children. 
1: deal with the node and then with all children (and then all children of these children) (breadth-first search or BFS)
2: deal with the node and then its first child (and subtree), second child (and subtree) etc (depth-first search of DFS)  

A visitor pattern is used to allow the algorithms to be separated from the object 
on which it operates and without modifying the objects structures (eg a visited flag can be 
owned by the algorithm)

The visitor pattern also allows the visit method to dynamically depend on both  the object and the visitor
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

    def get_value(self):
        return self.value
   
    def accept(self, visitor):
        visitor.visit(self)
           
    def set_children(self, children):
        '''set the children'''
        self.children = children

    def __repr__(self):
        '''unique string representation'''
        return str('node: {val} {children}'.format(
            val = self.value,
            children=self.children
            ) )
    

class DepthFirstSearch(object):
    
    def __init__(self,root, nodes, first_label=0):
        '''Perform the Depth First Search on nodes'''
        self.result=[]
        root.accept(self)
          
    def visit(self, node):
        '''visit one node.'''
        self.result.append(node.get_value())
        for node in node.children:
            node.accept(self)
            

class BreadthFirstSearch(object):
    
    def __init__(self,root, nodes, first_label=0):
        '''Perform the Breadth First Search through the nodes'''
        self.result=[]
        self.bfs_recursive([root])
          
    def visit(self, node):
        self.result.append( node.get_value() )
        
    def bfs_recursive(self,nodes):
        childnodes=[]
        if len(nodes) is 0:
            return         
        for node in nodes: #gather all nodes from next layer into childnodes before recursing
            node.accept(self)
            childnodes.extend(node.children)
            
        self.bfs_recursive(childnodes)
        

class TreeTestCase( unittest.TestCase ):

    def setUp(self):
        '''
        called before every test. 
        0 = is the head node
        left = up 
        right = down 
        that is: 1 2 3 are children of 0

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
        self.nodes[0].set_children( [self.nodes[1], self.nodes[2], self.nodes[3]])
        self.nodes[1].set_children( [self.nodes[4], self.nodes[5] ,self.nodes[6]])
        self.nodes[5].set_children( [self.nodes[7]])
        
        # decide on a root for the tests
        self.root = self.nodes[0]
        
        

    def test_DFS_visitor_pattern(self):
        
        DFS = DepthFirstSearch(self.nodes[0],self.nodes)
        # the result is equal to [0, 1, 4, 5, 7, 6, 2, 3,]
        self.assertEqual(DFS.result, [0, 1, 4, 5, 7, 6, 2, 3,] )

    def test_BFS_visitor_pattern(self):
            
        BFS = BreadthFirstSearch(self.nodes[0],self.nodes)
        # the result is equal to [0, 1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(BFS.result, range(8) )
    

if __name__ == '__main__':
    unittest.main()
