'''
Inter-Communication

Shared memory is a memory that can be accessed by one or more processes. But this is raise a problem in synchronization.

Message passing system is a method that provide mechansim for processes to communicate and sync their actions.
    A -> msg queue 
    B -> msg queue
    send(msg) or receive(msg)

    There must be a link such that communication can be established. This is usually something physical (hardware) like a cable or waves.
    
    There are blocking and non-blocking msgs.
    Blocking msgs are asynchronous and it waits untill something happens. Ex: m.aquire() -> wait indefinitely
    Non-blocking msgs are synchronous and it dosen't wait untill something happens. Ex: m.aquire(blocking=False) -> we need to know if it got time-out or got the value.
        Putting this in a loop will help with the checking process. Like 'if' statements.
'''