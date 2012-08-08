import fcntl
from multiprocessing import Process
import os
import time

def do_flock(fname):
    pid = os.getpid()
    f = open(fname, 'w')
    print '[%d] try lock' % pid
    fcntl.flock(f.fileno(), fcntl.LOCK_EX)
    print '[%d] locked' % pid
    time.sleep(1)
    f.close()
    #fcntl.flock(f.fileno(), fcntl.LOCK_UN | fcntl.FD_CLOEXEC)
    print '[%d] lock released' % pid

fname = 'hoge'
procs = []
for i in range(4):
    p = Process(target=do_flock, args=(fname,))
    p.start()
    procs.append(p)

for p in procs:
    p.join()
