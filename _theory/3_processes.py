'''
Process is a program that is in execution. It is different to program in that process is active.
And process is executed sequentially.

Process generally has a stack (temp storage), a heap(dynamic memory allocation) and a data section.

Process also has states, which includes: new, ready, waiting, running, terminated.

Process control block contains information such as the process state & number, program counter, registers...etc.

Concurrent events are those that happen at the same time from one source. In software, the concurrency happens due to the fast
switching between events. The speed in which it happens make it look like it is happening in parallel. But parallel are those that happen
at the same time with its own source.

The switching of events can happen via context. This context has the saved history of a process. And the switching introduces an overhead
as nothing else can happen while the switching is happening.

A process can have multiple threads. But this is parallel. Concurrency happens in one thread but with multiple processes being switched in fast speed.
Parent process creates a child process and so on. These are usually controlled and managed by a process identifier.

As an example, browsers are multiple process because when one tab stops working, it cannot affect other tabs.

There are three ways of starting a process. Fork, Forksever and Spawning. Spawning is the one to focus on. Other two is for Unix.
    Spawning is the creation of a completely new process including its own GIL. Because of this, for multiprocessing, __name__ == "__main__" is required
    to ensure which codes are intended for the main process.
    GIL is the global interpreter lock. It is produced 1 for each interpreter and it is used to ensure that no other process is being done on that interpreter.

Process pool is used to manage small number of child processes.
'''

import multiprocessing as mp
from multiprocessing import Pool
import time

def sayHello(name):
    """Simple function to print a name"""
    print("Name:", name)

def process():
    """Example of a longer running process"""
    print("Child")
    time.sleep(3)
    print("Child Stop")

def f(x):
    """Square function for pool demonstration"""
    return x*x

if __name__ == "__main__":
    # Example 1: Single process execution
    print("\n--- Single Process Example ---")
    print("Start")
    sayHello("Peter")
    print("Stop")

    # Example 2: Multiple process execution
    # It outputs the same message but through a child process that runs separately from the parent
    print("\n--- Multiple Process Example ---")
    print("Start")
    
    # Note that args has ',' at the end because the function only has one argument. 
    # By putting ',' we ensure that the input is tuple.
    # kwargs (keywords arg) can also be used. It expects dictionary.
    p1 = mp.Process(target=sayHello, args=("Peter",))
    
    # Start the process
    p1.start()
    
    # Stop the process
    # There are two modes for multiprocessing:
    # Daemonic processes terminate when the main process terminates - it dosen't block the main program from exiting
    # Non-daemonic (default) processes terminate only when their tasks are done
    p1.join()  # join([timeout]), if empty, is indefinite. If there is a number, it blocks at most timeout seconds
    print("Stop")

    # Example 3: Compare daemon and non-daemon processes
    print("\n--- Daemon Process Example ---")
    p2 = mp.Process(target=process)
    p2.daemon = True
    print("Start")
    p2.start()
    p2.join()  # p2.terminate() is also an option. This doesn't wait for the process to end.
    print("Stop")

    # Example 4: Process Pool example
    print("\n--- Process Pool Example ---")
    # Using 'with' ensures proper cleanup of pool resources
    with Pool(processes=4) as pool:
        # Map the square function over range(10) using 4 processes
        result = pool.map(f, range(10))
        print(f"Squared numbers: {result}")