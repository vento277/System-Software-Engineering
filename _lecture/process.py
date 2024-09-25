# A process is a program in execution. A task is processed linearly. Multi-processing aspect is that a task that acesses different availalble processes. 
# Task manager in our desktops can illustrate this nicely. 

# Process is more than the code. They include program counter, the content, stakc, data and heap.
# Program counter is the address of the next instruction
# content is the processor's registers
# Stack is the temprary data 

# The idea of concurrency

import multiprocessing as mp

def sayHello(name):
    print("Print")
    
# without __name__ == "__main__", the child process will run through the entire code and be kept in an infite loop.
# p1 = mp.Process(target = sayHello, arg = ("Peter",))
# p1.start()
# p1.join()

if __name__ == "__main__":
    print("This is the main process: beiginning")
    
    # This outputs the same thing as calling sayHello() but a completely different way of dealing the process.
    # This creates a child process that runs seperately for which the parent waits untill it finishes. Unlike
    # below, the process is always at the main level, and is not seperated it terms of process.
    # This is multiprocess way
    p1 = mp.Process(target = sayHello)
    p1.start()
    
    # join([Timeout]), if empty, is indefinite. If there is a number, it timeouts for that much time. for doucmentation in python '[]' means optional. 
    p1.join()
    
    # This is single process way 
    # sayHello()
    
    print("This is the main process: end")
    
    # Process class
    # positional argument is how we call function in C
    # python can use keyword based function call. for example if the function equires foo(a,b,c)
    # we can call it Process(target = sayHello, args("Victor",))
    # tuple vs list, mutability
    
    # Spawning,  create a seperate process, a completly new python interpretor and the enviionrment is created for it - including its own GIL.

# mp.Process(group = None, ...)
# Daemon is the process that continues untill the main process finises. This is an optional parameter in miltiprocessing. 
# so if it is a deamon process, if the main function terminates, everything terminates. 

# finally: (anything that has to be ran regardingless of exception for anything. for example clean-ups). 
# with: (resources and exceptional handling.)

# This code implements a parallel processing approach to validate a Sudoku puzzle.
# It uses Python's multiprocessing module to check columns, rows, and subgrids concurrently.

# The code assumes the following have been previously defined:
# - SIZE: The size of the Sudoku grid (likely 9 for a standard 9x9 Sudoku)
# - testcase: The Sudoku puzzle to be validated
# - checkColumn, checkRow, checkSubgrid: Functions to validate a column, row, and subgrid respectively
# - processes: An empty list to store the created processes
# - mp: The multiprocessing module (imported as 'mp')
