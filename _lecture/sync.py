# Semaphore is similar to the bahbior of mutex. threading.Semaphore(value=1)
# You can do __.semaphore(value = 1) or (1) or (2)
# _.aquire, aquires the semaphore
# _.release, releases a semaphore, incrementing the internal counter
# Why are we using semaphore instead of counter -> system supported counter with atomic 

# Deadlock
'''
This is really bad if it happends and it is terminal.

This happens when two or more tasks are waiting indefinitely for an action/event that is cuased by another waiting process
so neither of them can process. 
'''
import threading
def worker1(lock1, lock2):
    lock1.acquire()
    print("DEBUG")
    lock2.acquire()
    print("Critical")
    lock1.release
    lock2.release

def worker2(lock1, lock2):
    lock1.acquire()
    print("DEBUG")
    lock2.aqcuire()
    print("Critical")
    lock1.release
    lock2.release
    
if __name__ == "__main__":
    mutex1 = threading.Lock()
    mutex2 = threading.Lock()
    
    t1 = threading.Thread(target = worker1, args=(mutex1, mutex2))
    # t1 = threading.Thread(target = worker1) stills works beacuse threading locks are shared when delcared.
    # But by using args = (mutex1, mutex2), we can change the threading to multiprocessing without any chance. as
    # mutliprocessing dosen't share the locks.
    # Why is there comma at the end of the args is not needed beacuse there is two or more parameters which is for sure a tuple. 
    # Whereas one parameter, to make it a tuple, we add the comma. 
    t1.start()
        
    t2= threading.Thread(target = worker1, args=(mutex1, mutex2))
    t2.start()
    
    t1.join()
    t2.join()
    
    
# For there to be a deadlock,
# Mutual Exclusion, hold and wait (hold one that waits additional thats held by other process), no preemption, circular wait

# Critical section
# Mutual exclusion, ...
# Counters are the critical seciton

# Dining philosophers problem
# 
# 

# Semaphore is a variable or abstract data type used to control access to a common reousce by multhreading to avoid critical section problems in a concurrent system such as multiktasking operating system. 

# Mutex is a type of semaphore that supports mutual exclusion.