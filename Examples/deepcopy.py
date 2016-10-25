import copy

class Copy(object):
    def __init__(self):
        self.a = [1]
        self.b = [2]

    def __deepcopy__(self, memodict={}):
        newone = type(self)()
        newone.__dict__.update(self.__dict__)
        print newone.__dict__
        for attr, val in newone.__dict__.iteritems():
            if attr != 'a':
                setattr(newone, attr, copy.deepcopy(val, memodict))
        return newone
        
c = Copy()
d = copy.deepcopy(c)
print dir(d)

print 'a', id(c.a), id(d.a)
print 'b', id(c.b), id(d.b)
