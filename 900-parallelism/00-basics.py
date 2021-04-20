import multiprocessing

print("Number of cpu : ", multiprocessing.cpu_count())





"""
Classes for building parallel program
    Process
    Queue
    Lock
    
Process class
    set up another python process
    provide it to run code
    a way for the parent application to control execution
    functions
        start()
        join()
    define a worker function - this will be run by the process
    instantiate a process object and start processing via start()
        process will run and return its result
    tell the process to complete via join() function
        terminate the process
        without join(),
    
    
"""