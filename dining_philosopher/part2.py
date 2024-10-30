#student name: Peter Kim
#student number: 18693002

# Approach:
# A loop to ensure that each philosopher can only pick up both chopsticks if they are 
# simultaneously available.
#
# 1. Each philosopher is assigned two chopsticks: a "left" and a "right," represented by semaphores.
# 2. In each eating attempt, the philosopher tries to acquire the left chopstick first. If successful, 
#    it attempts to acquire the right chopstick immediately afterward.
# 3. If the philosopher fails to acquire the right chopstick, it releases the left chopstick and retries
#    the entire acquisition process after a brief delay.
# 4. Once both chopsticks are acquired, the philosopher proceeds to eat, then releases both chopsticks 
#    before resuming thinking.

import multiprocessing
import random #is used to cause some randomness 
import time   #is used to cause some delay to simulate thinking or eating times

def philosopher(id: int, chopstick: list): 
    """
       implements a thinking-eating philosopher
       id is used to identifier philosopher #id (id is between 0 to numberOfPhilosophers-1)
       chopstick is the list of semaphores associated with the chopsticks 
    """
    def eatForAWhile():   #simulates philosopher eating time with a random delay
        print(f"DEBUG: philosopher{id} eating")
        time.sleep(round(random.uniform(.1, .3), 2)) #a random delay (100 to 300 ms)
    
    def thinkForAWhile(): #simulates philosopher thinking time with a random delay
        print(f"DEBUG: philosopher{id} thinking")
        time.sleep(round(random.uniform(.1, .3), 2)) #a random delay (100 to 300 ms)

    for _ in range(6): #to make testing easier, instead of a forever loop we use a finite loop
        leftChopstick = id
        rightChopstick = (id + 1) % 5      #5 is number of philosophers

        # * Loop until both chopsticks are acquired
        while True:
            # * Attempt to acquire the left chopstick
            if chopstick[leftChopstick].acquire(block=False):
                # * If successful, attempt to acquire the right chopstick
                if chopstick[rightChopstick].acquire(block=False):
                    # * Successfully acquired both chopsticks and shows which philosopher has which pairs of chopsticks.
                    print(f"DEBUG: philosopher{id} has chopstick{leftChopstick}")
                    print(f"DEBUG: philosopher{id} has chopstick{rightChopstick}")
                    break
                else:
                    # * Release the left chopstick if the right one wasn't available
                    chopstick[leftChopstick].release()
                    
            # Small delay for debugging to avoid tight looping
            # time.sleep(random.uniform(0.01, 0.05))

        eatForAWhile()  #use this line as is

        print(f"DEBUG: philosopher{id} is to release chopstick{rightChopstick}")
        chopstick[rightChopstick].release()
        print(f"DEBUG: philosopher{id} is to release chopstick{leftChopstick}")
        chopstick[leftChopstick].release()

        thinkForAWhile()  #use this line as is

if __name__ == "__main__":
    semaphoreList = list()          #this list will hold one semaphore per chopstick
    numberOfPhilosophers = 5

    for i in range(numberOfPhilosophers):             
        semaphoreList.append(multiprocessing.Semaphore(1))    #one semaphore per chopstick

    philosopherProcessList = list()
    for i in range(numberOfPhilosophers): #instantiate all processes representing philosophers
        philosopherProcessList.append(multiprocessing.Process(target=philosopher, args=(i, semaphoreList)))
    for j in range(numberOfPhilosophers): #start all child processes
        philosopherProcessList[j].start()
    for k in range(numberOfPhilosophers): #join all child processes
        philosopherProcessList[k].join()