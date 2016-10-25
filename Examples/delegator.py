import inspect

def foo():
   print inspect.stack()[0][3]



def delegate(func):
    print inspect.stack()[1]
    def inner(self, *args, **kwargs):
        print self, inspect.stack()[0][3]
        for worker in self.workers:
            func(worker, *args, **kwargs)
    return inner

 
class Worker(int):
    def func1(self, stuff):
        print self, stuff

class Hello(object):

    def __init__(self):
        self.workers = map(Worker, range(5))
    
    @delegate
    def func1(self, stuff):
        funcname=inspect.stack()[0][3]
        getattr(self, funcname)(stuff)

hello = Hello()
hello.func1('coucou')




