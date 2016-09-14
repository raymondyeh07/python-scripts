
########################################################################
class Particle(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, v1, v2):
        """Constructor"""
        self.v1 = v1
        self.v2 = v2
        
    def __gt__(self, other):
        return self.v1 > other.v1
        
    def __lt__(self, other):
        return self.v1 < other.v1
    
    def __repr__(self):
        return 'Particle {} {}'.format(self.v1, self.v2)
        
    
