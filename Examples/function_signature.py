
def func(*args):
    flag = True
    if len(args)==1:
        toprint = 1
    elif len(args)==2:
        toprint, flag = args
    if flag:
        print toprint
    else:
        print 'printing forbidden'


func('Hello')
func('Hello', False)
func(True)
