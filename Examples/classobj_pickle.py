import pickle

class TestClass(object):
    def __init__(self):
        self.var = 2

out = open('testclass.pck', 'w')
pickle.dump(TestClass, out)
out.close()

infile = open('testclass.pck')
TestClass2 = pickle.load(infile)
t = TestClass2()
t.var
