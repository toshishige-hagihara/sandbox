
import signal
import time

### Main
class Test(object):
    def terminate(self, signum, frame):
        print 'terminate'

t = Test()
signal.signal(signal.SIGINT, t.terminate)

while True:
    print "I'm alive"
    time.sleep(5)
