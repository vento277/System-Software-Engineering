'''
Deadlock happens when entities are waiting indefinitely for something from one another such that neither can proceed.

The conditions are: Mutual exclusion, Hold and wait, No preemption and Circular Wait

To ensure dealock to not happen, we just need to make sure one of the conditino is not met.

For example, 
hold and wait can be avoided by ensureing that a process hold only that of which is requested and nothing else.
no preemptio can be avoided by releasing all the resource if requested resouce is not availalble immediately
no circular wait can be avoided by having some order of all source types

Starvation is when dealock consumes resources which prevents other processes to start. 

There are three typical problems of deadlock.
    - Producer-Consumer
    - Readers and Writers
    - Dinning Philosophers
'''
# Deadlock may happen due to the execution order/timing
import threading
def worker1(lock1, lock2):
    lock1.acquire()
    print("DEBUG: lock1 acquired, lock2 is next")
    lock2.acquire()
    print("In critical section")
    lock2.release()
    lock1.release()
def worker2(lock1, lock2):
    lock2.acquire()
    print("DEBUG: lock2 acquired, lock1 is next")
    lock1.acquire()
    print("In critical section")
    lock1.release()
    lock2.release()

# Deadlock is sure to happen
def worker3(lock1, lock2):
    lock1.acquire()
    print("DEBUG: lock1 acquired, waiting for lock2")
    while not lock2.locked(): pass #ensuring deadlock for demo
    lock2.acquire()
    print("In critical section")
    lock2.release()
    lock1.release()
def worker4(lock1, lock2):
    lock2.acquire()
    print("DEBUG: lock2 acquired, waiting for lock1")
    while not lock1.locked(): pass #ensuring deadlock for demo
    lock1.acquire()

if __name__ == "__main__":
    mutex1 = threading.Lock()
    mutex2 = threading.Lock()

    t1=threading.Thread(target=worker1, args=(mutex1, mutex2))
    t1.start()
    t2=threading.Thread(target=worker2, args=(mutex1, mutex2))
    t2.start()
    t1.join()
    t2.join()

    t3=threading.Thread(target=worker3, args=(mutex1, mutex2))
    t3.start()
    t4=threading.Thread(target=worker4, args=(mutex1, mutex2))
    t4.start()
    t3.join()
    t4.join()

