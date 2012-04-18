from functools import wraps
import sys

def v2s(version):
    return '.'.join([str(v) for v in version])

def version_validator(_min=None, _max=None):
    def _version_validator(function):
        @wraps(function)
        def __version_validator(*args, **kw):
            '''This is validator'''
            version = args[0]._version
            if (_min is not None and version < _min) or (_max is not None and _max < version):
                raise RuntimeError('Not supported for version %s' % v2s(version))
            res = function(*args, **kw)
            return res
        return __version_validator
    return _version_validator

class Hoge(object):
    def __init__(self, version):
        self._version = version

    @version_validator(_min=(2,0), _max=(3,0))
    def func1(self):
        '''This is func1'''
        print 'func1 called'
        pass

    @version_validator(_max=(3,0))
    def func2(self):
        '''This is func2'''
        print 'func2 called'
        pass

for version in [(1,9), (2,0), (3,0), (3,2)]:
    h = Hoge(version)
    print '-- version: %s' % v2s(version)
    try:
        h.func1()
    except:
        print 'Error:', sys.exc_info()[1]
    try:
        h.func2()
    except:
        print 'Error:', sys.exc_info()[1]
