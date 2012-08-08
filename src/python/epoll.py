
import os
from subprocess import Popen, PIPE
import select
import sys
import time

### Main
processes = {}
epoll = select.epoll()
for i in range(2):
    p = Popen(['/bin/sh', 'hoge.sh'], stdout=PIPE, stderr=PIPE)
    processes[i] = p
    epoll.register(p.stdout, select.EPOLLIN)

while True:
    fdset = [t[0] for t in epoll.poll()]
    for fd in fdset:
        data = os.read(fd, 1024)
        sys.stdout.write(data)
    time.sleep(5)
