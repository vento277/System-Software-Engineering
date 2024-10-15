
# Global Interpreter Lock
# Lock is important here. For python to work, there needs to be lock. In multiprocessing, GIL is not an issue. But it is an issue
# For multithreading. Because of this, multithreading uses one core. So why multithreading? 
# Lock has to be grabbed by the thread to run. So other threads are waiting for the lock. Release and aquire GIL.
# One thread for interpreter, one gil -> one process. This is not a problem in in multiprocessing beacuse of spawning as lock exists per interpretor. 
# Is multithreading useless? If CPU bound, multithreading it not good as they have to wait (in python), 
# I/O bound, multithreading workds well. 

# Process comes first. 

# Instead of spawning, it works under one process. Therefore, less resource intensive and less time consumming as things are shared. 
# Each thread has its own registers beacuse it needs its own calculation running.
# Thread has its own ID, and it is known globally in the computer. 

# Amdahl's Law
# Parts that can run in parallel, the speed up <= 1/(series run + (parallel run/N)), where parallel run = 1 - series run  

# Concurrency is not parallel. It only means that things are running in the same time, not always in parallel. Even
# in single core, if things switch fast enough, thing can be vired as concurrent. 
# Parallelism is specific. Things are running simulatenously. Multiple cores. 

# GPUs were not for processing. They have a lot of cores to display things - which has a lot of pixels which many cores helped. This
# structure hepled with machine learning as multiprocessing was there. 

# KNowing which is in parallel and which to run in series, is not easy. Balancing they division such that it is worth the trouble is
# also not easy. Data splitting and dependacy may be hard to handle. And testing and debugging get difficult as there are multiple
# execution paths. 

# I/O bound is that something that spends more time waiting for an I/O. Like CMD in windows.
# CPU bound is someting that spends more time doing instead of wating for I/O. -> Better for multiprocessing

# Cpython 

import threading

def worker():
    print("Hello")
    print(f"Hello {threading.current_thread().name}")
    
if __name__ == "__main__":
    for t in range(2):
        thread = threading.Thread(target= worker, name=f"worker{t}") # The first arugment has to be callable - like function. 
        thread.start()
    #thread.join() If there is no join(), deamonic = None. 
    
    # Creating three threads.
    # for i in range(3):
    #   thread.start()
    #   thread.join() now this join() 
    # for j in range(3):
    #   thread.start()
    #   thread.join() now this join() is bad beacuse it is making it sequential. 
    #   start -> end -> start... instead of start -> start -> start -> end -> end -> end
    
    # Now this won't work beacuse thread now is not a object of thread, and instead, is whatever start() returns.
    # You can't call join() from that. 
    #   thread = threading.Thread(target= worker).start()
    #   thread.join() 

# Daemon can be set during the instantication or later on. 


