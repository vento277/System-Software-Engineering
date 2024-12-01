import threading
import random 

class CircularBuffer:
    def __init__(self, size: int):
        self._buffer = [0] * size
        self._in_i = 0
        self._out_i = 0
    
    def insert(self, item: int):
        self._buffer[self._in_i] = item 
        self._in_i = (self._in_i + 1) % SIZE # Modulo to wrap around the i and make a circle. 

    def remove(self) -> int:
        item = self._buffer[self._out_i]
        self._out_i = (self._out_i + 1) % SIZE
        return item
    
    def read(self):
        return self._out_i

def producer() -> None:
    for i in range(SIZE):
        item = random.uniform(1,100)
        empty.acquire()
        with mutex:
            buffer.insert(item)
        full.release()
        print(f"{item} Produced")

def consumer() -> None:
    for i in range(SIZE):
        full.acquire()
        with mutex:
            item = buffer.remove()
        empty.release()
        print(f"{item} Consumed")

def reader() -> None:
    print(buffer.read())

if __name__ == "__main__":
    SIZE = 5
    buffer = CircularBuffer(SIZE)

    empty = threading.Semaphore(0)
    full = threading.Semaphore(SIZE)
    mutex = threading.Lock()  #lock for protecting data on insertion or removal

    reader1 = threading.Thread(target=reader)
    reader2 = threading.Thread(target=reader)
    reader3 = threading.Thread(target=reader)
    writer1 = threading.Thread(target=producer)
    writer2 = threading.Thread(target=consumer)

    reader1.start()
    reader2.start()
    reader3.start()
    writer1.start()
    writer2.start()

    reader1.join()
    reader2.join()
    reader3.join()
    writer1.join()
    writer2.join()



    
