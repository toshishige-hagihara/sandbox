import time

from multiprocessing import Process
from multiprocessing.managers import BaseManager

class Hoge(object):
    l = []

    def add(self, x):
        self.l.append(x)

    def get(self):
        return self.l

class MyManager(BaseManager):
    pass

def client():
    MyManager.register('hoge')
    m = MyManager(address=('127.0.0.1', 50000), authkey='abc')
    print 'start connecting'
    m.connect()
    print 'connected'
    h = m.hoge()
    print h.get()

MyManager.register('hoge', Hoge)
manager = MyManager(address=('127.0.0.1', 50000), authkey='abc')
manager.start()
manager.hoge().add(10)

Process(target=client).start()

while True:
    time.sleep(5)
