from multiprocessing import *

def sayHi2(n):
    i = 0
    while i < 10000000:
        i = i + 1
    print ("Hi", n, "from process", current_process().pid)

def manyGreetings():
    print("Hi from process", current_process().pid, "(main process)")
    name = "Jimmy"
    p1 = Process(target=sayHi2, args=(name,))
    p2 = Process(target=sayHi2, args=(name,))
    p3 = Process(target=sayHi2, args=(name,))

    p1.start()
    p2.start()
    p3.start()

#execute
manyGreetings()