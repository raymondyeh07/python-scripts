import pprint
import unittest 
from stack import Stack 

'''PolyTree with depth first and breadth first traversal algorithms

Each node may have several children. 
1: deal with the node and then with all children (with all subtrees) (breadth-first search or BFS)
2: deal with all children and finally with the node (depth-first search of DFS)  

A visitor pattern is used to allow the algorithms to be separated from the object 
on which it operates and without modifying the objects structures (eg a visited flag can be 
owned by the algorithm)

The visitor pattern also allows the visit method to dynamically depend on both  the object and the visitor

'''


class Node(object):
    '''
    Implements a polytree: 
    each node has an arbitrary number of children and parents
    There are no loops in the directed polytree
    '''
    
    def __init__(self, value):
        '''constructor. 
        value can be anything, even a complex object. 
        '''
        self.value = value   # wrapped object
        self.children = []
        self.parents = []
        self.undirectedlinks = [] #the union of the parents and children
        

    def getValue(self):
        return self.value
    
    def accept(self, visitor):
        visitor.visit(self)
             
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



class BreadthFirstSearch(object):
    
    def __init__(self,root, nodes, linktype):
        '''Perform the breadth first search of the nodes'''
    
        self.result=[]
        self.visited=dict()
        self.bfs_recursive([root],linktype)
        
          

    def visit(self, node):
        if self.visited.get(node, False):
            return
        self.result.append( node.getValue() )
        self.visited[node]=True
        

        
    def bfs_recursive(self,nodes, linktype ):
        '''Breadth first recursive implementation
        each recursion is one level down the tree
        linktype can be "children", "parents","undirected" '''
        linknodes=[]
        if len(nodes) is 0:
            return 
        
        for node in nodes: # collect a list of all the next level of nodes
            if (self.visited.get(node, False)):  
                continue              
            linknodes.extend(node.get_linked_nodes(linktype))        
        for node in nodes: #add these nodes onto list and mark as visited
            if (self.visited.get(node, False)):  
                continue            
            node.accept(self)
        
        self.bfs_recursive(linknodes,  linktype)

            


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
        self.set_link(self.nodes[3],self.nodes[6])
    

    def set_link(self, parent, child):
        '''set the parents child links'''
        parent.children.append(child)
        parent.undirectedlinks.append(child)
        child.parents.append(parent)                 
        child.undirectedlinks.append(parent)    
    
    def test_BFS_visitor_pattern_children(self):
        
        BFS = BreadthFirstSearch(self.nodes[0],self.nodes,"children")
          # the result is equal to [0, 1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(BFS.result, range(8) )

    def test_BFS_visitor_pattern_undirected(self):
            
        BFS = BreadthFirstSearch(self.nodes[0],self.nodes,"undirected")
        # the result is equal to [0, 1, 2, 3, 4, 5, 6, 9, 7, 8]
        self.assertEqual(BFS.result, [0, 1, 2, 3, 4, 5, 6, 9, 7, 8] )
    

if __name__ == '__main__':
    unittest.main()
