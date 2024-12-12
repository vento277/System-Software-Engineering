'''
A real-time system implies that there is something significant 
and important about its response time, and that involves real-time
scheduling. It gives some level of gurantee that the system responds 
within a specified time constraints (deadline).

There are two clsses of real-time systems:
    - Hard real-time systems which require a task to be serviced by its deadline. 
    Eg. Air-bag, Heart pacemaker
    - Soft real-time systems which do not consider as a failure when missing a deadline. 
    Through it will consider it as degraded when that happens. 
    Eg. web-browsing, media system

Embedded systems are specific-purpose (so not general-purpose) 
computing systems that are embedded within a bigger system. 

In a real-time system, tasks must be scheduled more strictly so that the 
required timeliness is achieved.

Scheduling is the task of selecting one process from among the 
processes in memory that are ready to execute, and allocate the CPU
to it.

CPU scheduling decisions may take place when a process:
    1. Switches from running to waiting state
    2. Switches from running to ready state
    3. Switches from waiting to ready state
    4. Terminates

1 and 4 is non-preemptive (or cooperative).
    CPU allotted to the process until its completion
2 and 3 is preemptive

Processes are generally divided into a number of CPU bursts.
In an IO-bound process, there are usually many short CPU bursts, 
but in a CPU-bound process, there are a few long CPU bursts.

When a process is selected by the scheduler, the dispatcher module gives control 
of the CPU to the process selected. This involves:

- Switching context
- Jumping to the proper location in the user program to restart that program

Scheduling algorithms criteria:
    Waiting time – amount of time a process has been waiting in the ready queue

    Arrive <--waiting--> Schceduled

    Turnaround time – amount of time to execute a particular process (includes waiting time in memory and ready queue, 
    executing in CPU and doing IO)

    Arrive <--waiting--> Schcedulded <--CPU, I/O--> Completion

    Response time – amount of time it takes from when a request was submitted until the first response is produced, 
    not the final/overall output.
        In an interactive system we may be interested in the response time (e.g., to see some early output)

    Arrive <--waiting--> Scceduleded <----> 1st response
        
    CPU utilization – keep the CPU as busy as possible
    Throughput – # of processes that complete their execution per time unit

For all schedluing algorithms, we aim to minimize or maximize optimization crtieria. 
    aim to minimize: turnaround time, or waiting time, or response time
    aim to maximize: CPU utilization, or throughput
    In most cases, we optimize for the average measure. 

Real-time systems are event driven -> meaning that they wait for an event to happen. 
This could cause a latency in that there is a spread between the event being serviced and the event being occured. 
There are two latencies that affects performance. 
One is the dispatch and other is interrupt latency. 

Interrupt latency is the time from the arrival of interrup to the start of the routine that serfices interrup.
Dispatch latency is the time it takes for a dispatcher to take the current process off and move to other CPU.

Schedulling Algos:
First-Come, First Served - Whoever comes first are processed first.
P1 - 3
P2 - 24
P3 - 3

0 - 3 - 27 - 30
Waiting time = (0 + 3 + 27) / 3 

Shortest-Job_First - Whichever has the shortest job-time gets to go first (optimal)
P1 - 3
P2 - 24
P3 - 4

0 - 3 - 7 - 31
W = (0 + 3 + 7) / 3

Priority - Which ever job has the highest prioiry (lower integer) gets to go first
One of the problem with this is that there may be a chance where lower priority job waits indefinitely. 
To fix this, we incrementally increase the priority of a job as the time passes, thereby aging the job.
This way, the priority naturally increases and thus there is little chance that low priority job waits indefinitely. 
P1 - 3 -> Pr = 2
P2 - 12 -> Pr = 1
P3 - 5 -> Pr = 3

0 - 12 - 15 - 20
W = (0 + 12 + 15)/3

Round-Robin - Get the job done in FCFS but with time quantum steps (fixed step sizes)
P1 - 12
P2 - 2
P3 - 4
Time Quantum = 4

  P1  P2  P3  P2  
0 - 4 - 6 - 10 - 14 - 18
W = ((10 - 4) + 4 + 6) / 3

We can evalute the performance of the algo in these ways:
Deterministic modelling where one test against known workload and performance (What we did above but with same P1, P2...etc)
Queueing model where one uses mathematical model to test the algo
Simulation where one compares the models by running multiple simulations

Multilevel Queue partitions the queue into separate queues. It it common to divide them up in foreground and background processes.
Here, each process is assign to a queue and each queue may have its own algo for the schedules. This way optimizaion is done better.
One can also set a prioiry among the partitioned queues or set a fixed amount of time allocation to use the CPU. The former may lead to starvation.

If multiple cores are availalble, one can share the load. This allows for load balancing. 
Also allow soft affinity where a process can migrate between processors.
Memory stall is the time it takes for a processor to access its data when accessing a memory.


'''