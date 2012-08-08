from threading import Timer
import time

def hello():
    print 'hello'

t = Timer(2, hello)
t.start()
print 'hoge'
t.cancel()
#while True:
#    time.sleep(1)
