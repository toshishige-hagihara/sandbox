import time

from multiprocessing import Process, Queue, Manager
import os

q = Queue()
m = Manager()
#d = m.dict()
d = {}

pid = os.fork()
if pid:
    i = 0
    while True:
        if 'hoge' in d:
            print d['hoge']
        while not q.empty():
            i = q.get()
            print i
        time.sleep(1)
else:
    while True:
        d['hoge'] = 'hagi'
        q.put('qq')
        time.sleep(1)
