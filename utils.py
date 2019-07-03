import threading

class ThreadHandler():
    STEP = 0.2

    def __init__(self, target):
        self.lock = threading.Lock()
        self.stop = threading.Event()
        args = (self.lock, self.stop)
        self.thread = threading.Thread(target=target, args=args)

    def start(self):
        self.thread.start()

    def setStop(self):
        self.stop.set()

    def join(self):
        while self.thread.is_alive():
            try:
                self.thread.join()
            except KeyboardInterrupt:
                self.stop.set()