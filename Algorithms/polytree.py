import pprint
import unittest 
from stack import Stack 

'''PolyTree with depth first and breadth first traversal algorithms

Each node may have several children. 
Each node may have several parents.

The PolyTree is directed and acyclic. It may have multiple roots ( a node without a parent)


The traversal algorithms are implemented as separate functions, 
following a simple visitor pattern. 

BFS and DFS for children of the node
1: deal with the node and then with all children (with all subtrees) (breadth-first search or BFS)
2: deal with all children and finally with the node (depth-first search of DFS)  

BFS and DFS for parents of the node
3: deal with the node and then with all children (with all subtrees) (breadth-first search or BFS)
4: deal with all children and finally with the node (depth-first search of DFS)  

full polytree search
5: breadth first from the node treating it as an undirected tree 
6: breadth first search with root nodes coming first children later 




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
    each node has an arbitray number of children and also an arbitray number of parents
    '''
    
    def __init__(self, value):
        '''constructor. 
        value can be anything, even a complex object. 
        '''
        self.value = value   # wrapped object
        self.children = []
        self.parents = []
        self.undirectedlinks =  [] # ask colin about best Python way to deal with this
        self.visited = False
      
    def visit(self):
        return self.value

    def set_children(self, children):
        '''set the children'''
        self.children = children
        self.undirectedlinks.extend(children)
        
    def set_parents(self, parents):
        '''set the parents'''
        self.parents = parents
        self.undirectedlinks.extend(parents)
        
    def get_linked_nodes(self, type):  #ask colin, I imagine there is a more elegant Python way to do this
        if (type is "children"):
            return self.children
        if(type is "parents"):
            return self.parents
        if(type is "undirected"):
            return self.undirectedlinks
            
         

    def __repr__(self):
        '''unique string representation'''
        
        return str('node: {val} {children}'.format(
            val = self.value,
            children=self.children
            ) )

class NodeSquared(Node):
    def visit(self):
        return self.value**2

    
def bfs_children_recursive(nodes, result):
    '''pre-order, recursive implementation
    each recursion is one level down the tree'''
    bfs_base_recursive(nodes, result,"children")

def bfs_parents_recursive(nodes, result):
    '''pre-order, recursive implementation
    each recursion is one level down the tree'''
    bfs_base_recursive(nodes, result,"parents")
 

       
def bfs_recursive(nodes,result, linktype ):
    '''pre-order, recursive implementation
    each recursion is one level down the tree
    linktype can be "children", "parents","undirected" '''
    linknodes=[]
    if len(nodes) is 0:
        return 
    for node in nodes:
        if not node.visited:
            result.append( node.visit() )
    for node in nodes:
        if not node.visited:
            linknodes.extend(node.get_linked_nodes(linktype))
            node.visited=True
    bfs_recursive(linknodes, result, linktype)

def bfs_iterative(nodes, result,linktype):
    '''breadth first iterative implementation
     each iteration is one level down the tree
     linktype can be "children", "parents","undirected" 
     visited flag is used for "undirected" '''    
    linknodes=[]
    while len(nodes):
        for node in nodes:
            if not node.visited:
                result.append( node.visit() )
                
        for node in nodes:
            if not node.visited:
                node.visited=True
                linknodes.extend(node.get_linked_nodes(linktype))
        nodes=linknodes
        linknodes=[]

    
def dfs_recursive(root, result, linktype):
    '''depth first search recursive implementation
    each recursion is one level down the tree'''
    if root is None:
        return 
    result.append( root.visit() )
    root.visited=True
    for node in root.get_linked_nodes(linktype):
        if (not node.visited): 
            dfs_recursive(node, result, linktype)
        

def dfs_iterative(root, result, linktype):
    '''depth first search iterative implementation
        in same order as for recursion
     visited flag is used for "undirected" '''    
    todo = Stack()
    todo.append(root)
    while len(todo):
        node = todo.pop()
        result.append(node.visit())
        node.visited=True;
        for node in reversed(node.get_linked_nodes(linktype)): #reversal makes it match dfs_recursive
            if (not node.visited):            
                todo.append(node)
        

def dfs_iterative_2(root, result,linktype):
    '''depth first search iterative implementation
        children are traversed in a different order to previous algorithms (but its more efficient)
        ''' 
    todo = Stack()
    todo.append(root)
    while len(todo):
        node = todo.pop()
        result.append(node.visit())
        node.visited=True;
        for node in node.get_linked_nodes(linktype):
            if (not node.visited):     
                todo.append(node)
        



class TreeTestCase( unittest.TestCase ):

    def setUp(self):
        '''
        called before every test. 
        0 and 8 are root/head nodes
        
        
        8
         \
          \
           9
            \
             \
              4  
             /  
            /  
           1--5--7
          / \
         /   \
        0--2  6
         \   /
          \ /
           3
           
           
        
        '''
        # building all nodes
        self.nodes = dict( (i, Node(i) ) for i in range(10) )
        
        self.set_link(self.nodes[0],self.nodes[1])
        self.set_link(self.nodes[0],self.nodes[2])
        self.set_link(self.nodes[0],self.nodes[3])
        self.set_link(self.nodes[1],self.nodes[4])
        self.set_link(self.nodes[1],self.nodes[5])
        self.set_link(self.nodes[1],self.nodes[6])
        self.set_link(self.nodes[5],self.nodes[7])
        self.set_link(self.nodes[8],self.nodes[9])
        self.set_link(self.nodes[9],self.nodes[4])
        
    def set_link(self, parent, child):
            '''set the parents child links'''
            parent.children.append(child)
            parent.undirectedlinks.append(child)
            child.parents.append(parent)                 
            child.undirectedlinks.append(parent)    
                        
    def test_bfs_recursive(self):
        result = []
        bfs_recursive( [self.nodes[0]], result,"children" )
        # the result is equal to [0, 1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(result, range(8) )        
    
    def test_bfs_recursive(self):
                result = []
                bfs_recursive( [self.nodes[0]], result,"children" )
                # the result is equal to [0, 1, 2, 3, 4, 5, 6, 7]
                self.assertEqual(result, range(8) )           

    def test_bfs_iterative(self):
        result = []
        bfs_iterative( [self.nodes[7]], result ,"parents")
        # the result is equal to [7, 5, 1, 0]
        self.assertEqual(result, [7, 5, 1, 0] )
        
    def test_bfs_iterative_2(self):
        result = []
        bfs_iterative( [self.nodes[1]], result ,"undirected")
        # the result is equal to [1, 0, 4, 5, 6, 2, 3, 9, 7, 8]
        self.assertEqual(result, [1, 0, 4, 5, 6, 2, 3, 9, 7, 8] )
    

    def test_dfs_recursive(self):
        result = []
        dfs_recursive( self.nodes[0], result,"children" )
        # the result is equal to [0, 1, 4, 5, 7, 6, 2, 3]
        self.assertEqual(result, [0, 1, 4, 5, 7, 6, 2, 3])
   
    def test_dfs_iterative(self):        
        result = []
        dfs_iterative( self.nodes[4], result, "undirected")
        # the result is equal to [4, 1, 9, 0, 8]
        self.assertEqual(result, [4, 1, 0, 2, 3, 5, 7, 6, 9, 8])
        
    def test_dfs_iterative_2(self):        
            result = []
            dfs_iterative_2( self.nodes[4], result, "parents" )
            # the result is equal to  #for this algoritm more "natural" to do children "backwards"
            self.assertEqual(result, [4, 9, 8,  1, 0])
if __name__ == '__main__':
    unittest.main()
