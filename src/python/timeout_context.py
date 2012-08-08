import os
import signal
from subprocess import Popen
from threading import Timer
import time
from traceback import format_exc

class TimeoutError(RuntimeError):
    pass

class TimeoutContext():
    def __init__(self, timeout, timeout_msg, fn=None, *args, **kwargs):
        def handler(signum, frame):
            msg = timeout_msg
            try:
                if fn is not None:
                    fn(*args, **kwargs)
            except Exception:
                msg = format_exc() + msg
            raise TimeoutError(msg)

        def timeout_signal():
            os.kill(os.getpid(), signal.SIGUSR1)

        self._pre_handler = signal.getsignal(signal.SIGUSR1)
        self._handler = handler
        self.t = Timer(timeout, timeout_signal)

    def __enter__(self):
        signal.signal(signal.SIGUSR1, self._handler)
        self.t.start()

    def __exit__(self, exc_type, exc_value, traceback):
        signal.signal(signal.SIGUSR1, self._pre_handler)
        self.t.cancel()

def cleanup(p):
    if p.poll() is None:
        p.terminate()

p = Popen(['sh', 'hoge.sh'])
with TimeoutContext(3, 'Timeout', cleanup, p):
    p.communicate()
    raise RuntimeError('Hoge')
    while True:
        print 'Im alive'
        time.sleep(1)
        break

print 'Im alive'
