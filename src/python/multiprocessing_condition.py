import time

from multiprocessing import Process, Condition
import os

cond = Condition()

def wait_condition():
    cond.acquire()
    cond.wait()
    print '[%d] waked!' % os.getpid()
    cond.release()

for i in range(3):
    Process(target=wait_condition).start()

time.sleep(1)
print 'notify!'
cond.acquire()
cond.notify_all()
cond.release()
