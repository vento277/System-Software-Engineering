#student name: Peter Kim
#student number: 18693002

import threading
import random #is used to cause some randomness 
import time   #is used to cause some delay in item production/consumption

class circularBuffer: 
    """ 
        This class implement a barebone circular buffer.
        Use as is.
    """
    def __init__ (self, size: int):
        """ 
            The size of the buffer is set by the initializer 
            and remains fixed.
        """
        self._buffer = [0] * size   #initilize a list of length size
                                    #all zeroed (initial value doesn't matter)
        self._in_index = 0   #the in reference point
        self._out_index = 0  #the out reference point

    def insert(self, item: int):
        """ 
            Inserts the item in the buffer.
            The safeguard to make sure the item can be inserted
            is done externally.
        """
        self._buffer[self._in_index] = item
        self._in_index = (self._in_index + 1) % SIZE

    def remove(self) -> int:
        """ 
            Removes an item from the buffer and returns it.
            The safeguard to make sure an item can be removed
            is done externally.
        """
        item = self._buffer[self._out_index]
        self._out_index = (self._out_index + 1) % SIZE
        return item

def producer() -> None:
    """
        Implement the producer function to be used by the producer thread.
        It must correctly use full, empty and mutex.
    """
    def waitForItemToBeProduced() -> int: #inner function; use as is
        time.sleep(round(random.uniform(.1, .3), 2)) #a random delay (100 to 300 ms)
        return random.randint(1, 99)  #an item is produced

    for _ in range(SIZE * 2): #we just produce twice the buffer size for testing
        item = waitForItemToBeProduced()  #wait for an item to be produced
        print(f"DEBUG: {item} produced")
        
        # Start of student code
        
        # The buffer starts empty, thus, 'empty' semaphore can be acquired at the start.  
            
        # Decrements empty semaphore by 1.
        # If empty is 0, it will wait for the consumer to remove an item.
        # If not, the producer will add an item.
        empty.acquire()
        
        # Critical section
        # By locking and releasing mutex, ensure the consumer is not removing while producer is adding. 
        with mutex:
            buffer.insert(item)
        
        # Increments full semaphore by 1.
        # It signals that the buffer has an additional item. 
        full.release()
        
        # End of student code

def consumer() -> None:
    """
        Implement the consumer function to be used by the consumer thread.
        It must correctly use full, empty and mutex.
    """
    def waitForItemToBeConsumed(item) -> None: #inner function; use as is
        time.sleep(round(random.uniform(.1, .3), 2)) #a random delay (100 to 300 ms)
        #to simulate consumption, item is thrown away here by just ignoring it
        
    for _ in range(SIZE * 2): #we just consume twice the buffer size for testing
        
        # Start of student code
        
        # Decrements full semaphore by 1.
        # If full is 0, it will wait for producer to add an item.
        # If not, the consumer will remove(consume) an item.
        full.acquire() 
        
        # Critical section
        # By locking and releasing mutex, ensure the producer is not adding when consumer is removing.
        with mutex:
                item = buffer.remove()
        
        # Increments empty semaphore by 1. 
        # It signals that the buffer has an additional space.     
        empty.release()
        
        # End of student code
        
        #use the following code as is
        waitForItemToBeConsumed(item)  #wait for the item to be consumed
        print(f"DEBUG: {item} consumed")

if __name__ == "__main__":
    SIZE = 5  #buffer size
    buffer = circularBuffer(SIZE)  #initialize the buffer

    full = threading.Semaphore(0)         #full semaphore: number of full buffers
                                          #initial value set to 0
    empty = threading.Semaphore(SIZE)     #empty semaphore: number of empty buffers
                                          #initial value set to SIZE
    mutex = threading.Lock()  #lock for protecting data on insertion or removal

    # Start of student code
    producer = threading.Thread(target=producer)  # Producer thread
    consumer = threading.Thread(target=consumer)  # Consumer thread
    
    # Start both threads
    producer.start() 
    consumer.start()
    
    # Wait for both threads to complete
    producer.join()
    consumer.join()
    # End of student code