from ctypes import cdll
from Queue import Queue
from threading import Thread
import time

lib = cdll.LoadLibrary('./libfoo.so')

class Foo(object):
    def __init__(self):
        self.obj = lib.Foo_new()

    def bar(self):
        lib.Foo_bar(self.obj)

def buffered(reader, size):
    """Creates a buffered data reader.
    The buffered data reader will read and save data entries into a buffer.
    Reading from the buffered data reader will proceed as long as the buffer
    is not empty.
    
    Args:
        reader: the data reader to read from.
        size: max buffer size.
    
    Returns:
        The buffered data reader.
    """

    class EndSignal():
        pass

    end = EndSignal()

    def read_worker(r, q):
        for d in r:
            q.put(d)
        q.put(end)

    def create_reader():
        r = reader()
        q = Queue(maxsize=size)
        t = Thread(
            target=read_worker, args=(
                r,
                q, ))
        t.daemon = True
        t.start()
        e = q.get()
        while e != end:
            yield e
            e = q.get()

    return create_reader

def cpu_bound_reader():
    a = 0
    for j in xrange(1000):
        start_time = time.time()
        for i in xrange(5000000):
            a = i
        elapsed_time = time.time() - start_time
        print time.time(), "python single read time:", elapsed_time
        yield j

f = Foo()
r = buffered(cpu_bound_reader, 10)
start_time = time.time()
wait_time = time.time()
for idx, e in enumerate(r()):
    elapsed_time = time.time() - start_time
    # mini batch size 5
    if idx > 0 and idx % 5 == 0:
        print time.time(), "wait time for mini batch data:", time.time() - wait_time
        f.bar()
        wait_time = time.time()
    
    print time.time(), "python buffered read time:", elapsed_time
    start_time = time.time()
