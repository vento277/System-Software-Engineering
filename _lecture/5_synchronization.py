'''
CONCURRENCY AND SYNCHRONIZATION CONCEPTS:
---------------------------------------
Data Consistency in Concurrent Programming:
- Data inconsistency is a critical issue in multiprocessing/threading when multiple processes/threads access shared resources
- Processes in an OS can be independent (isolated) or cooperating (shared resources)

Race Conditions:
- Occurs when program behavior depends on the relative timing or interleaving of multiple threads/processes
- Results in unpredictable outcomes when accessing shared resources

Critical Section:
- Section of code where shared resources are accessed
- Has three parts: entry section, critical section, exit section
- Requires proper synchronization to prevent race conditions

Critical Section Solutions:
1. Mutual Exclusion: Only one thread can execute in critical section at a time
2. Progress: If no thread is in critical section, a thread wanting to enter should be able to
3. Bounded Waiting: Limits on how long a thread must wait to enter critical section

Synchronization Mechanisms:
1. Locks: Block access to code sections ensuring exclusive access
2. Semaphores: Counter-based synchronization that can control multiple concurrent accesses
   - Binary Semaphore: Acts like a mutex lock (0 or 1)
   - Counting Semaphore: Allows fixed number of threads to access resource

Problems to Avoid:
- Busy Waiting: Thread repeatedly checks condition in a loop, wasting CPU cycles
- Deadlock: Two or more threads waiting for each other indefinitely
- Starvation: Thread never gets access to resource
'''

import multiprocessing
import threading
import time

class SharedData:
    def __init__(self):
        self.data: int = 0
        
    def increment(self):
        """Unsafe increment demonstrating race condition"""
        x = self.data
        x += 1
        time.sleep(0.2)  # to emulate possible behaviour
        self.data = x
        
    def increment_sync(self):
        """Safe increment using Lock"""
        lock.acquire()
        x = self.data
        x += 1
        time.sleep(0.2)  # to emulate possible behaviour
        self.data = x
        lock.release()
        # or
        # Lock gets acquired and released automatically using 'with'
        # with lock:
        #   ...
        
    def increment_sync2(self):
        """Safe increment using Semaphore"""
        s.acquire()
        x = self.data
        x += 1
        time.sleep(0.2)  # to emulate possible behaviour
        self.data = x
        s.release()

def worker():
    """Demonstrate process/thread variable access"""
    try:
        print(f"Trying to access var: {var}")
    except NameError:
        print("Nope, doesn't have access")
    else:
        print(f"Has access to var: {var}")

def task(name):
    print(f"{name} is trying to acquire the semaphore...")
    with binary_semaphore:  # This will block if the semaphore is already acquired
        print(f"{name} has acquired the semaphore.")
        time.sleep(2)  # Simulating resource usage
        print(f"{name} is releasing the semaphore.")

if __name__ == "__main__":
    # Process vs Thread variable access demonstration
    var = "hello"
    multiprocessing.Process(target=worker).start()
    threading.Thread(target=worker).start()
    
    # Initialize shared data and synchronization objects
    y = SharedData()
    lock = threading.Lock()
    s = threading.Semaphore(1) # Binary semaphore
    s2 = threading.Semaphore(3) # Counting semaphore with a maximum of 3
    
    # Example 1: No synchronization - demonstrates race condition
    print("\nExample 1: No synchronization")
    t1 = threading.Thread(target=y.increment)
    t2 = threading.Thread(target=y.increment)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"The shared data's final value: {y.data}")
    
    # Example 2: With Lock synchronization
    print("\nExample 2: With Lock synchronization")
    t3 = threading.Thread(target=y.increment_sync)
    t4 = threading.Thread(target=y.increment_sync)
    t3.start()
    t4.start()
    t3.join()
    t4.join()
    print(f"The shared data's final value: {y.data}")
    
    # Example 3: With Semaphore synchronization
    print("\nExample 3: With Semaphore synchronization")
    t5 = threading.Thread(target=y.increment_sync2)
    t6 = threading.Thread(target=y.increment_sync2)
    t5.start()
    t6.start()
    t5.join()
    t6.join()
    print(f"The shared data's final value: {y.data}")

    # Example 4: Only one thread can hold the semaphore at a time, meaning only one thread can access the shared resource.
    binary_semaphore = threading.Semaphore(1)
    threads = [threading.Thread(target=task, args=(f"Thread-{i}",)) for i in range(3)]

    # Start threads
    for thread in threads:
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Example 5: Up to three threads can hold the semaphore concurrently, allowing three threads to access the shared resource simultaneously.
    counting_semaphore = threading.Semaphore(3)
    threads = [threading.Thread(target=task, args=(f"Thread-{i}",)) for i in range(5)]

    # Start threads
    for thread in threads:
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()
