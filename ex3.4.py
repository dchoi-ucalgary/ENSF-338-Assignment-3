import threading
import random
import time

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.head = self.tail = -1
        self._lock = threading.Lock()

    def lock(self):
        self._lock.acquire()

    def unlock(self):
        self._lock.release()

    def enqueue(self, data):
        while True:
            self.lock()
            if (self.tail + 1) % self.size == self.head:
                # queue is full, wait and try again
                self.unlock()
                time.sleep(1)
            else:
                if self.head == -1:
                    # queue is empty
                    self.head = 0
                    self.tail = 0
                    self.queue[self.tail] = data
                else:
                    self.tail = (self.tail + 1) % self.size
                    self.queue[self.tail] = data
                self.unlock()
                return

    def dequeue(self):
        while True:
            self.lock()
            if self.head == -1:
                # queue is empty, wait and try again
                self.unlock()
                time.sleep(1)
            else:
                data = self.queue[self.head]
                self.queue[self.head] = None
                if self.head == self.tail:
                    # queue is now empty
                    self.head = -1
                    self.tail = -1
                else:
                    self.head = (self.head + 1) % self.size
                self.unlock()
                return data

def producer():
    while True:
        # generate a random number between 1 and 10
        data = random.randint(1, 10)
        # wait for that many seconds
        time.sleep(data)
        # enqueue the number to the queue
        q.enqueue(data)

def consumer():
    while True:
        # generate a random number between 1 and 10
        data = random.randint(1, 10)
        # wait for that many seconds
        time.sleep(data)
        # dequeue a number from the queue and print it to the terminal
        print(q.dequeue())

if __name__ == '__main__':
    q = CircularQueue(5)
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()