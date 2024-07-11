# IO Model

*PS: here introduce the I/O model in UNIX-Like system*

## Blocking IO


When call is made, the thread will block until the execution complete. This means the thread will do nothing until data is received or sent


advantage: not cost cpu in low-concurreny environment, due to the thread will been removed from running queue of os.


disadvantage:

If using blocking IO, every IO request will create a thread, so it will create lots of threads in high-concurrency scenaio. specific, this will cause several problem:

1. high memoy-usage. Every thread occupy 1M RAM in windows, and 8M RAM in linux.
2. cost of context switching. A high number of thread switches leads to substantial context switching overhead.


## NonBlocking IO


read in a loop, the cpu wiil be cost


## IO Multiplexing


### select


### poll


### epoll


## Signal-Driven



## Asynchronous IO
