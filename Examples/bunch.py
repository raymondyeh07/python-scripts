class Bunch(dict):
    def __init__(self, **kw):
        super(Bunch, self).__init__(**kw)
        self.__dict__ = self

if __name__ == '__main__':
    b = Bunch(a=1, b=2)
    print b
