### What is Big Data?

Big Data is either:
* __High Volume__:  Data so large that it can’t be managed by a single computer
* __High Velocity__ - Data coming in and going out too quickly to be processed by a single computer (think real-time processing real-fast)
* __High Variety__ - Data in many different formats (largely unstructured: text, videos, log files, etc.)

How Big is too big?
* __Small__: < 10 GB, Fits in a single machine's memory (i.e. thousands of sales figures)
* __Medium__: 10 GB - 1 TB, Fits on one machine's disk (i.e. millions of web pages)
* __Large__: > 1 TB, needs to be stored across multiple machines (i.e. billions of web clicks)

### What is the difference between local and distributed systems?

Local uses the computational resource of 1 machine. Distributed uses the computational resources of multiple machines.

Local System
* simplistic, less complex

Distributed System
* scalable (easy to add more machines than cores to a machine)
* fault tolerant (if one machine fails the whole network is not down)

### What is the general structure of a distributed systems architecture / storage system?

A distributed system has one "master" and many "slaves". The storage system has one "name" node and several data nodes.


### What are the storage mechanisms behind Distributed File Systems?

1. Individual files are broken up into blocks
2. A given number of replicas of each block are stored across the cluster (on data nodes)
3. If any of those replicas is lost, the name node replicates one of the remaining copies so that the replication factor remains the same

### What is MapReduce?

MapReduce is a means to process information stored across several machines without having to move data between machines. MapReduce __moves the code to where the data is located__ instead of moving the data to the code.

### Hadoop

* Parallelization & Distribution (input splits)
* Partitioning (shuffle & sort)
* Fault-tolerance
* Resource Management
* Status and monitoring

__How does Hadoop MapReduce work?__
1. Split task into many subtasks
2. Solve these tasks independently
3. Recombine the subtasks into a final result

__Map Function__
1. Data is read in as key-value pairs
2. Data is filtered & transformed
3. Data is passed on to the reduce step as key-value pairs

__Reduce Function__
1. Data is read in as key-value pairs, where every value for a given key has been aggregated into a list (i.e. all the records with the same key end up on the same reducer).
2. All values in the value list are combined (reduced) in some way.
3. Data is output as key-value pairs, stored in multiple files. 
