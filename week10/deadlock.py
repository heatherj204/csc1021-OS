import threading
import random
import time

class Philosopher(threading.Thread):

    running = True

    def __init__(self, xname, forkOnLeft, forkOnRight):
        threading.Thread.__init__(self)
        self.name = xname
        self.forkOnLeft = forkOnLeft
        self.forkOnRight = forkOnRight

    def run(self):
        while(self.running):
            # pilosopher is thinking
            time.sleep(random.uniform(3,13))
            print(f'{self.name} is hungary')
            self.dine()

    def dine(self):
        fork1, fork2 = self.forkOnLeft, self.forkOnRight

        while self.running:
            fork1.acquire(True)
            locked = fork2.acquire(False)
            if locked: break
            fork1.release()
            print(f'{self.name} swaps forks')
            fork1, fork2 = fork2, fork1
        else:
            return

        self.dining()
        fork2.release()
        fork1.release()

    def dining(self):
        print(f'{self.name} starts eating')
        time.sleep(random.uniform(3,13))
        print(f'{self.name} finishes eating and leaves to think')

def dingingPhilosophers():
    forks = [threading.Lock() for n in range(5)]
    philosopherNames = ('John', 'Mary', 'Jim', 'Anna', 'David')
    philosophers = [Philosopher(philosopherNames[i], forks[i % 5], forks[(i + 1) % 5]) \
            for i in range(5)]

    random.seed(507129)
    Philosopher.running = True
    for p in philosophers: p.start()
    time.sleep(100)
    Philosopher.running = False
    print("Now we're finishing")

dingingPhilosophers()
