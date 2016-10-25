
class GrandFather(object):
    def __init__(self):
        print 'GrandFather', 0

class Father(GrandFather):
    def __init__(self, *args, **kwargs):
        super(Father, self).__init__()
        print 'Father', 0

class Mother(GrandFather):
    def __init__(self, val):
        super(Mother, self).__init__()
        print 'Mother', val 

class Child(Mother, Father):
    def __init__(self, val):
        super(Child, self).__init__(val)
        print 'Child', val


c = Child(1)
