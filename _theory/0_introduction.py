'''
Software Design for Engineers II

Overview of Operating Systems

An operating system (OS) is a critical component that serves as a resource allocator 
and provides essential services for managing computer operations. Key functions include:

- Process Management: Overseeing the execution of processes and threads.
- Memory Management: Allocating and deallocating memory as needed.
- Protection: Ensuring the integrity and security of data and processes.

The OS acts as an intermediary between the user and the hardware, abstracting complex operations. 
Examples of popular operating systems include MacOS, Windows, and Linux.

When computer starts, bootstrap program is loaded which is typically loaded in ROM.
Bootstrap initializes CPU registers, memory content, I/O...etc.

OS provides two types of services. 
First are thoes that is helpful to the user. These include:
1. UI (Command-Line and GUI)
2. Program execution 
3. I/O operations (USB or a file)
4. File-system (read or write)
5. Communications
6. Error detection

Second are thoes that are not helpful to the user but ensure efficiency:
1. Resource allocation (manage concurrent processes)
2. Accounting (keep track of which are using how much)
3. Protection and Security (manage access to data)

Prcess management is the allocation of resources such that it accomplishes a task. 
- Create and delete processes
- Suspend and resume processes
- Mechanism for sychronization, communication and deadlock

Memory management
- Track memory usage
- Decide which process should be used in the memory
- Allocate and deallocate memory spaces

Storage management
- 
----

This course will primarily focus on process management, covering the following topics:
1. Process vs. Thread
   - Understand the distinction between processes (independent execution units) 
     and threads (lightweight subprocesses that share resources).
2. Inter-Process Communication (IPC)
   - Explore methods for processes to communicate and synchronize their actions.
3. Synchronization
   - Investigate techniques for coordinating concurrent processes to prevent race conditions.
4. Deadlock Handling

We will also implement multi-tasking concepts using Python, which include:
1. Multi-Processing
- Learn how to create separate processes that can run concurrently.
2. Multi-Threading
- Understand how to use threads for parallel execution within a single process.
3. Communication Mechanisms
- Examine methods for data sharing and communication between processes and threads.
4. Synchronization Mechanisms
- Study techniques for ensuring proper sequencing and access control in multi-threaded applications.

We will also explore various types of operating systems, with a focus on real-time systems:
1. Real-Time Systems
   - Understand systems where timing is critical, requiring strict scheduling.
2. Hard Real-Time Systems
   - Learn about systems that must complete tasks by a defined deadline without exception.
3. Soft Real-Time Systems
   - Explore systems where tasks should ideally meet deadlines but can tolerate some delays.

The course will also include discussions on:
- Software Life Cycle
  - Examine the stages of software development from conception to deployment and maintenance.
- Testing
  - Understand various testing methodologies to ensure software quality and reliability.
- Agile Development
  - Discuss the principles of Agile methodologies and their application in software engineering.
- Unified Modeling Language (UML)
  - Introduce UML as a standard way to visualize the design of a system.
'''