class Hoge(object):
    def get(self):
        print 'get'

    def __getattr__(self, name):
        if name == 'do_GET':
            return self.get

def check_attr(o, name):
    if hasattr(o, name):
        print '%s has %s' % (o, name)
    else:
        print '%s does not have %s' % (o, name)

h = Hoge()
check_attr(h, 'do_GET')
getattr(h, 'do_GET')()
