'''
THREADING CONCEPTS:
------------------
Process was assumed that it ran on one thread. But a process can have multiple threads.
The difference lies in that multiprocessing uses one resource per process whereas multithreading shares resources within a process.
Threads share data within their process, making synchronization much more critical to prevent race conditions.

A thread is a subprocess that allows multiple sequences of operations to run concurrently within a single process.
Threads share the same memory space, which makes them more efficient than separate processes for resource sharing and communication.

Why choose threads over processes?
--------------------------------
1. Shared Memory: When data sharing is crucial (e.g., user data handling), threads are preferred as they naturally share memory
2. Resource Efficiency: Thread creation is much more lightweight than process creation
3. Limited Cores: If multiple CPU cores are limited, threading might be more practical than multiprocessing
4. Overhead Concerns: When the overhead of inter-process communication would be too high

Four Main Benefits of Threading:
------------------------------
1. Responsiveness: Keep UI responsive while handling background tasks
2. Resource Sharing: Efficient sharing of resources within the same process
3. Economy: Less overhead compared to creating new processes
4. Scalability: Better resource utilization for certain types of applications

Performance Considerations:
-------------------------
- Amdahl's Law describes the theoretical speedup in latency of the execution of a task at fixed workload
  that can be expected of a system whose resources are improved.
- CPU bound tasks (video editing, gaming) benefit more from multiprocessing
- I/O bound tasks (disk operations, network calls) benefit more from multithreading
- Due to Python's GIL (Global Interpreter Lock), threads are executed one at a time even on multi-core machines
- Thread ID is assigned by the OS as a non-negative integer for system-wide unique identification

Critical Threading Concepts Not Mentioned Above:
---------------------------------------------
1. Race Conditions: When multiple threads access shared data simultaneously
2. Deadlocks: When threads are waiting for each other indefinitely
3. Thread Synchronization Methods: Locks, RLocks, Semaphores, Events, Conditions
4. Thread Pooling: Managing a pool of worker threads for task execution
'''

import threading
import time
import random
from queue import Queue
from concurrent.futures import ThreadPoolExecutor

# Example 1: Basic thread-local storage
def worker(data):
    """Demonstrate thread-local storage usage"""
    try:
        print(f"Thread {threading.current_thread().name}: Initial value = {data.value}")
    except AttributeError:
        print(f"Thread {threading.current_thread().name}: No value yet")
        data.value = random.randint(1, 100)
        print(f"Thread {threading.current_thread().name}: Set value = {data.value}")

# Example 2: Daemon vs Non-daemon threads
def daemon():
    """Demonstrate daemon thread behavior"""
    print("Daemon thread starting")
    time.sleep(1)
    print("Daemon thread exiting")

def non_daemon():
    """Demonstrate non-daemon thread behavior"""
    print("Non-daemon thread starting")
    print("Non-daemon thread exiting")

# Example 3: Thread synchronization with Lock
def synchronized_worker(lock, shared_resource):
    """Demonstrate thread synchronization with a lock"""
    with lock:
        print(f"Thread {threading.current_thread().name} accessing shared resource")
        shared_resource['count'] += 1
        time.sleep(0.1)  # Simulate some work
        print(f"Shared resource count: {shared_resource['count']}")

# Example 4: Thread pool usage
def pool_worker(x):
    """Worker function for thread pool example"""
    time.sleep(0.1)  # Simulate some work
    return x * x

if __name__ == "__main__":
    print("\n--- Example 1: Thread Local Storage ---")
    local_data = threading.local()
    local_data.value = 2024
    print("Main thread value:", local_data.value)
    threads = []
    for _ in range(2):
        t = threading.Thread(target=worker, args=(local_data,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    print("\n--- Example 2: Daemon vs Non-daemon Threads ---")
    d = threading.Thread(target=daemon, daemon=True)
    t = threading.Thread(target=non_daemon)
    d.start()
    t.start()
    # Daemon threads typically don'y need join as it terminates when the main function terminates. 
    # Including join() makes the daemic character useless.
    # d.join()  
    t.join()  # Wait for non-daemon thread to complete

    print("\n--- Example 3: Thread Synchronization ---")
    lock = threading.Lock()
    shared_resource = {'count': 0}
    sync_threads = []
    for _ in range(5):
        t = threading.Thread(target=synchronized_worker, args=(lock, shared_resource))
        sync_threads.append(t)
        t.start()
    for t in sync_threads:
        t.join()

    print("\n--- Example 4: Thread Pool ---")
    with ThreadPoolExecutor(max_workers=3) as executor:
        numbers = list(range(5))
        results = list(executor.map(pool_worker, numbers))
        print(f"Thread pool results: {results}")

    print("\nAll examples completed")