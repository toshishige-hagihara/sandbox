import atexit
from subprocess import Popen

p = Popen(['/bin/sh', 'hoge.sh'])

def terminate(process):
    if p.poll is None:
        process.terminate()

atexit.register(terminate, p)
