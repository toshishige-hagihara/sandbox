from threading import Thread
import time

class Test(Thread):
    def __init__(self, *args, **keywords):
        self._count = 0
        super(Test, self).__init__(*args, **keywords)

    def alive(self):
        print "I'm alive: %d" % self._count

    def run(self):
        while True:
            self._count += 1
            time.sleep(1)

t = Test()
t.alive()
t.setDaemon(True)
t.start()
while True:
    t.alive()
    time.sleep(1)
