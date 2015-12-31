import pprint
import unittest 
from stack import Stack 

'''Binary tree with standard traversal algorithms.

Each node has two children. Therefore, when visiting a given node, 
it is possible to: 
1: deal with the current node, then its left child (the left subtree), 
and then its right child (pre-order)
2: deal with the left child, the current node, and the right child (in-order)
3: deal with the left child, the right child, and the current node (post-order)

In the case of a tree with an arbitrary number of children (not binary), 
in-order would not make sense, and there are two traversal algorithms: 
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
for better performance. In this module, I played with several implementations.

Exercises carried out by Alice: 
- post-order recursive and iterative algorithms, with their test cases 

'''


class Node(object):
    '''
    Implements a binary tree: 
    each node has two children, left and right.

    Important: There is no need for a Tree class. 
    Actually, the Node is equivalent to the subtree rooted at this node.
    '''
    
    def __init__(self, value):
        '''constructor. 
        value can be anything, even a complex object. 
        '''
        self.value = value   # wrapped object
        self.left = None     # left child 
        self.right = None    # right child
        self.visited = False
        # not necessary for standard visitors, and inelegant.
        # indeed,  it is good to able to call another visitor on the same nodes
        # without having to re-initialize the nodes.

    def visit(self):
        return self.value

    def set_children(self, left, right):
        '''set both the left and right children'''
        self.left = left
        self.right = right

    def __repr__(self):
        '''unique string representation'''
        left = 'null'
        right = 'null'
        if self.left:
            left = self.left.value
        if self.right:
            right = self.right.value
        return str('node: {val} {left} {right}'.format(
            val = self.value,
            left = left,
            right = right
            ) )

class NodeSquared(Node):
    def visit(self):
        return self.value**2

    
def preorder_recursive(node, result):
    '''pre-order, recursive implementation'''
    if node is None:
        return 
    result.append( node.visit() )
    preorder_recursive(node.left, result)
    preorder_recursive(node.right, result)


def preorder_iterative(root, result):
    '''pre-order, iterative implementation'''
    todo = Stack()
    todo.append(root)
    while len(todo):
        node = todo.pop()
        if node.right:
            todo.append(node.right)
        if node.left:
            todo.append(node.left)
        result.append( node.visit() )


def inorder_recursive(node, result):
    '''in-order, recursive implementation'''
    if node is None:
        return 
    inorder_recursive(node.left, result)
    result.append( node.visit() )
    inorder_recursive(node.right, result)


def inorder_iterative_visit1(root, result):
    '''
    in-order, iterative implementation.
    
    requires a visited flag to be added to each node.
    not very elegant, but obvious solution to cycling problem.
    In python I don't think this solution is better than the recursive one,
    because we still have a stack -> so mem usage is the same.
    In C++ or java, the stack should be declared on the heap...
    otherwise I don't see what is the gain. 
    '''
    todo = Stack()
    todo.append( root )
    while len(todo):
        node = todo.peek()
        if node:
            if not node.visited:
                node.visited = True
                todo.append( node.left )
            else:
                result.append( node.visit() ) # changed to node.visit to make more general
                todo.pop()
                todo.append( node.right )
        else:
            print 'none'
            todo.pop()


def inorder_iterative_visit2(root, result):
    '''cleaner and more understandable than visit1, but there is still 
    a visited flag'''
    todo = Stack()
    todo.append( root )
    while len(todo):
        node = todo.pop()
        if node:
            if not node.visited:
                node.visited = True
                todo.append( node ) # re-adding the node for second visit
                todo.append( node.left )
            else:
                result.append( node.visit() ) # changed to node.visit to make more general
                todo.append( node.right )


def inorder_iterative(root, result):
    '''Finally, without the visited flag... 
    took me some time to find this one...'''
    todo = Stack()
    todo.append( root )
    last = None
    while len(todo):
        node = todo.pop()
        if node:
            if not last or (last.left is node or last.right is node):
                todo.append( node )
                todo.append( node.left )
            else:
                result.append( node.visit() ) # changed to node.visit to make more general
                todo.append( node.right )
            last = node 


def postorder_recursive(node, result):
    '''post-order, recursive implementation'''
    if node is None:
        return 
    postorder_recursive(node.left, result)
    postorder_recursive(node.right, result)
    result.append( node.visit() )


def postorder_iterative_1(root, result):
    '''We effectively find the nodes from last to first
    so when we find each node we append to the start of the result not the back    
    This version uses visited'''
    todo = Stack()
    todo.append( root )
    while len(todo):
        node = todo.peek()
        if node:
            if not node.visited:
                node.visited = True
                result.insert(0,node.visit()) #add to back
                todo.append( node.right )
            else:
                todo.pop()
                todo.append( node.left )
        else:
            todo.pop()


def postorder_iterative(root, result):
    '''version without visited
    we find the nodes from last to first
    so each node is inserted at the start of the result not the back
    an alternative might be to reverse the result at the end'''  
    todo = Stack()
    todo.append( root )
    last = None
    while len(todo):
        node = todo.peek()
        if node:
            if not last or last.right is node or last.left is node:
                result.insert(0,node.visit())
                todo.append( node.right )
            else:
                todo.pop()
                todo.append( node.left )
            last=node
        else:
            todo.pop()
        

class BinaryTreeTestCase( unittest.TestCase ):

    def setUp(self):
        '''
        called before every test. 
        left = up 
        right = down 
        that is: 2 is the left child of 4, and 5 its right child

            0
           / \
          2   1
         / \
        4   3
         \
          5
        '''
        # building all nodes
        self.nodes = dict( (i, Node(i) ) for i in range(6) )
        # setting children. note that each node keeps track of its children,
        # no need for the polytree class
        self.nodes[4].set_children( self.nodes[2], self.nodes[5] )
        self.nodes[2].set_children( self.nodes[0], self.nodes[3] )
        # here setting the right child directly:
        self.nodes[0].right = self.nodes[1]
        # decide on a root for the tests
        self.root = self.nodes[4]

    def test_inorder_recursive(self):
        result = []
        inorder_recursive( self.root, result )
        # the result is equal to [0, 1, 2, 3, 4, 5]
        self.assertEqual(result, range(6) )

    def test_preorder_recursive(self):
        result = []
        preorder_recursive( self.root, result )
        self.assertEqual(result, [4, 2, 0, 1, 3, 5] )

    def test_preorder_iterative(self):
        result = []
        preorder_iterative( self.root, result )
        self.assertEqual(result, [4, 2, 0, 1, 3, 5] )

    def test_inorder_iterative_1(self):
        result = []
        inorder_iterative( self.root, result )
        self.assertEqual(result, range(6) )
 
    def test_inorder_iterative_2(self):
        result = []
        inorder_iterative( self.root, result )
        self.assertEqual(result, range(6) )
 
    def test_postorder_recursive(self):
        result = []
        postorder_recursive( self.root, result )
        self.assertEqual(result, [1, 0, 3, 2, 5, 4] )

    def test_postorder_iterative(self):
        result = []
        postorder_iterative( self.root, result )
        self.assertEqual(result, [1, 0, 3, 2, 5, 4] )

    def test_postorder_iterative_1(self):
        result = []
        postorder_iterative_1( self.root, result )
        self.assertEqual(result, [1, 0, 3, 2, 5, 4] )

if __name__ == '__main__':
    unittest.main()
