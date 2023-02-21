import threading


def worker():
    """thread worker function"""
    print(threading.get_ident())  # threading.get_ident() Return the ‘thread identifier’ of the current thread.


threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start() # start thread
