from multiprocessing import Manager, Queue, Process
import os
from Queue import Empty
import sys
from threading import Thread
import time

q = Queue()

def put():
    while True:
        print 'put'
        q.put('hoge')
        time.sleep(1)

def get():
    while True:
        try:
            print q.qsize()
            print q.get(timeout=1)
        except Empty:
            print 'empty'
            pass

t = Thread(target=get)
t.daemon=True
t.start()

#t2 = Thread(target=put)
#t2.daemon=True
#t2.start()
#Process(target=put).start()
#while True:
#    time.sleep(1)
pid = os.fork()
if not pid:
    q.put('hoge')
    #time.sleep(1)
    sys.exit(0)
else:
    pid = os.fork()
    if not pid:
        q.put('hoge')
        os._exit(0)
    else:
        while True:
            time.sleep(1)
