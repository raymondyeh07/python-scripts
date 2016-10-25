#----------------------------------------------------------------------
MODE = 'ee'

def set_mode(mode):
    """"""
    global MODE
    MODE = mode
    
    from particle import Particle
    
    # in real project, this will affect the P4 class
    # change the printout according to the mode: 
    def new_repr(self):
        return 'Particle {} {} {}'.format(MODE, self.v1, self.v2)
    Particle.__repr__ = new_repr
    
    # change the P4 sorting strategy: 
    if MODE == 'ee':
        Particle.__gt__ = lambda x, y: x.v1 > y.v1
        Particle.__lt__ = lambda x, y: x.v1 < y.v1
    elif MODE == 'pp':
        Particle.__gt__ = lambda x, y: x.v2 > y.v2
        Particle.__lt__ = lambda x, y: x.v2 < y.v2
        
    
    # how to deal with delta R?
    # could : add a polar method to P4, and use this one in deltar it it
    # exists
    # or change the basic deltar functions to use theta or eta
    
    # should this module change the classes, or should the classes
    # import this module? e.g. P4 could import collider.
