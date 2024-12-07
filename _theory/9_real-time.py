'''
A real-time system implies that there is something significant and important about its response time, and that involves real-time
scheduling. It gives some level of gurantee that the system responds within a specified time constraints (deadline).

There are two clsses of real-time systems:
- Hard real-time systems which require a task to be serviced by its deadline. Eg. Air-bag, Heart pacemaker
- Soft real-time systems which do not consider as a failure when missing a deadline. Throuhg it will consider it as degraded when that happens. Eg. web-browsing, media system

Embedded systems are specific-purpose (so not general-purpose) computing systems that are embedded within a bigger system. 

In a real-time system, tasks must be scheduled more strictly so that the required timeliness is achieved.

Scheduling is the task of selecting one process from among the processes in memory that are ready to execute, and allocate the CPU
to it.

CPU scheduling decisions may take place when a process:
1. Switches from running to waiting state
2. Switches from running to ready state
3. Switches from waiting to ready state
4. Terminates

1 and 4 is non-preemptive (or cooperative) - Once the CPU has been allocated to a process, the process keeps the CPU until it releases the CPU either by
terminating or by switching to the waiting state.
2 and 3 is preemptive

Rpocess is generally divided into a number of CPU bursts.
In an IO-bound process, there are usually many short CPU bursts, but in a CPU-bound process, there are a few long CPU bursts.

When a process is selected by the scheduler, the dispatcher module gives control of the CPU to the process selected
- switching context
- jumping to the proper location in the user program to restart that program

Dispatch latency is the time it takes for the dispatcher to stop one process and start another running

scheduling algorithms criteria:
    Waiting time – amount of time a process has been waiting in the ready queue

    Arrive <--waiting--> Schceduled

    Turnaround time – amount of time to execute a particular process (includes waiting time in memory and ready queue, executing in CPU and doing IO)

    Arrive <--waiting--> Schcedulded <--CPU, I/O--> Completion

    Response time – amount of time it takes from when a request was submitted until the first response is produced, not the final/overall output.
        In an interactive system we may be interested in the response time (e.g., to see some early output)

    Arrive <--waiting--> Scceduleded <----> 1st response
        
    CPU utilization – keep the CPU as busy as possible
    Throughput – # of processes that complete their execution per time unit

For all schedluing algorithms, we aim to minimize or maximize optimization crtieria. 
    aim to minimize: turnaround time, or waiting time, or response time
    aim to maximize: CPU utilization, or throughput
    In most cases, we optimize for the average measure. 

Real-time systems are event drive -> meaning that they wait for an event to happen. 
This could cause a latency in that there is a spread between the event being serviced and the event being occured. 

There are two latencies that affects performance. One is the dispatch and other is interrupt latency. 
Interrupt latency is the time from the arrival of interrup to the sart of the routine that serfices interrup.


'''