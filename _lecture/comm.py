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
        
    Queue needs temporary savings.
        Zero capacity (queue max length is zero, i.e., 0 messages). Sender must wait for the receiver
        Bounded capacity (finite length of n messages). Sender must block if the link is full, otherwise it can continue without waiting
        Unbounded capacity (infinite length). Sender never waits

    Client-Server model is the primary model for the internet.
        Sever is the service providing, like a file or the web And clients are thoes that require the service.
        
        Socket is the end point of communication. 
            Transmission control protocol. This is connection oriented, meaning that a connection has to be first be connected. It ensures that data is delivered.
                Like internet itself.
            User datagram protocol. This is connectionless, meaning that connection is not established at first. It dosen't guranteee that data is delivered.
                Like telephone calls or online streaming.

        Pipes are another mechanism for communication.

        Procedure calls are procedure calls between processes on netowkred systems.
            Endian describes the order of bytes of a word ina computer ememory. 

'''