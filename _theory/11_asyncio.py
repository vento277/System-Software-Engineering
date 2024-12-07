'''
Asynchronous I/O is another approach to multitasking. It falls under cooperative multitasking. Cooperative multitasking is when another control flow signals the context switch.
This is often called coroutines. Think of an external clock signal.

Asyncio is used when there is a need for light multitasking with large I/Os. 

Event loop continuously checks for the async tasks.
'''
import asyncio

    
async def mySleep(seconds: int):
    print(f"Going to sleep for {seconds}s")
    await asyncio.sleep(seconds)
    print(f"Back after {seconds}s")
    
    
async def add(a: int, b: int):
    return a + b

async def Answer():
    return 40

async def main(): # creating coroutine. Note that this is not executable on its own. 
    print("Hello...")
    await asyncio.sleep(1) # pauses coroutine untill the task of the await is done. 
    print("World!")
    
    # Here you can notice even the order is 2 5 1, it prints 1 2 5 as the tasks executes in that order. 
    task1 = asyncio.create_task(mySleep(2)) # If it can be used in an await expression, it is called an awaitable. 
    task2 = asyncio.create_task(mySleep(5))
    task3 = asyncio.create_task(mySleep(1))
    await task1
    await task2
    await task3
    
    # gather can be used to collect information. Returns list. 
    sum = await asyncio.gather(add(1, 2), add(2, 3))
    print(sum)

with asyncio.Runner() as runner: # this is a context manager that simplifies calling multiple async function in the same context. 
    asyncio.run(main()) # execute in the event loop