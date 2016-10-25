
########################################################################
class Particle(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, v1, v2):
        """Constructor"""
        self.v1 = v1
        self.v2 = v2
        
    def __gt__(self, other):
        import collider2
        if collider2.MODE == 'pp':
            return self.v1 > other.v1
        elif collider2.MODE == 'ee':
            return self.v2 > other.v2
        
    def __lt__(self, other):
        import collider2
        if collider2.MODE == 'pp':
            return self.v1 < other.v1
        elif collider2.MODE == 'ee':
            return self.v2 < other.v2

    
    def __repr__(self):
        import collider2
        if collider2.MODE == 'ee':
            return 'Particle {} {} {}'.format(
                'ee', 
                self.v1,
                self.v2)
        elif collider2.MODE == 'pp':
            return 'Particle {} {} {}'.format(
                'pp', 
                self.v1,
                self.v2)
            
    
