import threading
import urllib.request as urllib2
import random
import time
class Producer(threading.Thread):

    def __init__(self, integers, condition):

        threading.Thread.__init__(self)
        self.integers = integers
        self.condition = condition

    def run(self):
        while True:
            integer = random.randint(0, 256)
            self.condition.acquire()
            print(f'condition acquired by {self.name}')
            self.integers.append(integer)
            print(f'{integer} appended to list by {self.name}')
            print(f'condition notified by {self.name}')
            self.condition.notify()
            print(f'condition released by {self.name}')
            self.condition.release()
            time.sleep(1)

class Consumer(threading.Thread):

    def __init__(self, integers, condition):
        threading.Thread.__init__(self)
        self.integers = integers
        self.condition = condition

    def run(self):
        while True:
            self.condition.acquire()
            print(f'condition release by {self.name}')
