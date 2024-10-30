#student name: Peter Kim
#student number: 18693002

# Approach: 
# Limit the seat to 4 while providing equal oppertunity.
# 
# For each philosopher (0-4):
#     For each cycle (0-5):
#         1. limit.acquire()          --> First tries to get a "seat at table" (only 4 can proceed)
#         2. leftChopstick.acquire()  --> Gets left chopstick
#         3. rightChopstick.acquire() --> Gets right chopstick
#         4. eat()                    --> Eats
#         5. rightChopstick.release() --> Puts down right chopstick
#         6. leftChopstick.release()  --> Puts down left chopstick
#         7. limit.release()          --> Gives up "seat at table"
#         8. think()                  --> Thinks (OUTSIDE the limited section)
#
# For example:
# Time T1: Phil0, Phil1, Phil2, Phil3 acquire seats (Phil4 waits)
# Time T2: Phil0 finishes eating, releases seat, starts thinking
# Time T3: Phil4 can now acquire the released seat while Phil0 thinks
# Time T4: Phil1 finishes, releases seat while Phil0 is still thinking
# Time T5: Phil0 (finished thinking) can compete with Phil4 for next seat

import multiprocessing
import random #is used to cause some randomness 
import time   #is used to cause some delay to simulate thinking or eating times

def philosopher(id: int, chopstick: list, limit): 
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
        
        # * Try to get a seat at the table before picking up chopsticks
        #   Ensure no more than 4 can proceed with eating
        limit.acquire()
        
        leftChopstick = id
        rightChopstick = (id + 1) % 5      #5 is number of philosophers

        #to simplify, try statement not used here
        chopstick[leftChopstick].acquire()
        print(f"DEBUG: philosopher{id} has chopstick{leftChopstick}")
        chopstick[rightChopstick].acquire()
        print(f"DEBUG: philosopher{id} has chopstick{rightChopstick}")

        eatForAWhile()  #use this line as is

        print(f"DEBUG: philosopher{id} is to release chopstick{rightChopstick}")
        chopstick[rightChopstick].release()
        print(f"DEBUG: philosopher{id} is to release chopstick{leftChopstick}")
        chopstick[leftChopstick].release()

        # * Release the seat at the table after eating and giving up the chopsticks.
        #   Allow another to acquire the semaphore and begin eating
        limit.release()
        
        thinkForAWhile()  #use this line as is

if __name__ == "__main__":
    semaphoreList = list()          #this list will hold one semaphore per chopstick
    numberOfPhilosophers = 5

    # Allow only 4 philosophers to sit at the same time. 
    PhilosopherLimit = multiprocessing.Semaphore(4)

    for i in range(numberOfPhilosophers):             
        semaphoreList.append(multiprocessing.Semaphore(1))    #one semaphore per chopstick

    philosopherProcessList = list()
    for i in range(numberOfPhilosophers): #instantiate all processes representing philosophers
        # * By passing the limit semaphore, we ensure that no more than 4 philosophers 
        #   can attempt to eat simultaneously, while providing equal opportunity for each philosopher.
        #   Philosopher who didn't get the seat have to wait untill one of the seated philosopher finishes eating
        #   and releases the semaphore.
        philosopherProcessList.append(multiprocessing.Process(target=philosopher, args=(i, semaphoreList, PhilosopherLimit)))
    for j in range(numberOfPhilosophers): #start all child processes
        philosopherProcessList[j].start()
    for k in range(numberOfPhilosophers): #join all child processes
        philosopherProcessList[k].join()