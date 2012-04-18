### Doc string could be overwriten!
from functools import wraps

def mydeco1(function):
    def _mydeco(*args, **kw):
        '''this is mydeco1'''
        return function(*args, **kw)
    return _mydeco

@mydeco1
def test1(arg):
    '''this is test1'''
    print arg

test1(1)
print test1.__doc__

def mydeco2(function):
    @wraps(function)
    def _mydeco(*args, **kw):
        '''this is mydeco2'''
        return function(*args, **kw)
    return _mydeco

@mydeco2
def test2(arg):
    '''this is test2'''
    print arg

test2(2)
print test2.__doc__
