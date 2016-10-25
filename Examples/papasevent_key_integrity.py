
class PapasEvent(object):
    
    #----------------------------------------------------------------------
    def __init__(self, adict):
        """"""
        self.collections = adict
        
    #----------------------------------------------------------------------
    def add_collection(self, collection):
        """"""
        ids = set(collection)
        if len(ids) > 1:
            raise ValueError('More than one type')
        the_id = ids.pop()
        if the_id in self.collections:
            raise ValueError('type already present')
        self.collections[the_id] = collection
        
        

import unittest

class Test(unittest.TestCase):
    
    def setUp(self):
        self.papasevent = PapasEvent({1: 1, 2: 2})
    
    def test_mix(self):
        self.assertRaises(ValueError, 
                          lambda: self.papasevent.add_collection({1: 1, 2: 2}))
    
    def test_already(self):
        self.assertRaises(ValueError, 
                          lambda: self.papasevent.add_collection({1: 1}))
    
    def test_ok(self):
        self.papasevent.add_collection({3: 1})
        self.assertEqual(3, len(self.papasevent.collections))
    
    
if __name__ == '__main__':
    unittest.main()
    
        
