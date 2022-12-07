Title: My Jobs Aren't Running
Date: 11/28/22
Authors: Nick Carter
slug: my-jobs-arent-running
 
It's (sadly) fairly common for our RC machines to get into states where they aren't able to start new jobs.  Here are some ways to figure out what's going on if your jobs seem to be stuck in the queue

## Step 1: Check the state of the machines in the partition
The command 'sinfo -p _partitionname_' will generate a table showing the overall state of the machines in the partition.  The two most relevant fields in the table are the "AVAIL" and "STATE" fields.  "AVAIL" should always have the value "up".  If it doesn't, something has gone badly wrong; contact RC to get it looked at.  
The "STATE" field can have multiple values.  Each line in the table will have a different value in the "STATE" field, and the "NODELIST" field will list the machines in the partition that have that state.  The values you're likely to see in the "STATE" field are:  
*alloc: Machines in the "alloc" state are fully-occupied with jobs from our group.  If there are jobs waiting for the partition, all of the machines should be in this state.  
*mix: Machines in the "mix" state are some combination of idle, running our jobs, and running jobs from one of the "requeue" partition.  This state generally indicates that the machine(s) are healthy, and that there isn't enough work from our group to keep them full.  If machines stay in the "mix" state for a long time (more than 30 minutes) while our jobs are waiting, it may indicate a problem.  
*up: This indicates that Slurm thinks the machine(s) are operating correctly, but has no work to assign no them.  In practice, you're unlikely to see this state except during winter break, because there's almost always work in the requeue partition to be done.  If you see this state while there are jobs waiting to be run, something's gone wrong; contact RC to get it looked at.  
*down: Machines in this state are unavailable to run jobs; contact RC to get the issue looked into.  
*drain: This state indicates that Slurm is killing jobs from one of the requeue partitions to make room for jobs from our group.  This is the correct behavior as long as machines don't get stuck in this state for more than 30 minutes, in which case it may indicate a problem.  You should investigate further and contact RC if there is a problem.  
*drng: Machines in this state are overloaded with work, so Slurm is not scheduling further jobs until the load on them decreases.  This is generally a problem, most often caused by someone running jobs that start more threads/use more cores than they requested from Slurm.  If you see this, investigate further to figure out which user is causing the problem.  If they're from our group, contact them.  If the problematic jobs are from a requeue partition, contact RC and they'll deal with it.
## Step 2: Check the queue  
'squeue -p _partitionname_' will show a list of all the jobs queued for and running on the partition, as well as the username of the person who submitted them.  If your jobs aren't running because someone else is using all of the cores in the partition, this will tell you who is responsible and whether it's one person or several people filling up the partition.  Note that we don't guarantee that there will always be free cores in our partition, and there may be times when you just have to wait.  If one person is filling up the whole partition, it's reasonable to go talk to them about freeing up some nodes.  
Squeue can also be useful for figuring out whose jobs are overloading a node that's in the 'drng' state.
## Step 3: Investigate 'drng' nodes  
If one or more of the machines in a partition are stuck in the 'drng' state, the command 'lsload | grep _machinename_'  will show the load on the machine and let you figure out if the machine is in that state because it's overloaded.  (If a machine is in the 'drng' state and not overloaded, something has gone badly wrong and you should contact RC.)
Lsload will return an output of the form:  
'holy2c14201        40     10   25.0   2.86    191    133   MIXED'  
In this line, the first value is the name of the machine, the second (40 in this example) is the number of cores in the machine, and the fifth (2.86 here) is the load on the machine, which is a combination of the number of threads running on the machine and how much work each of those threads are doing.  Thus, the load can be a non-integer value if some of the threads on the machine spend some of their time waiting for data to be read from disk or idle for other reasons.  
If the load on the machine is greater than the number of cores, Slurm considers the machine overloaded and will not schedule any more jobs on the machine until the load drops.  The most common cause of this is that one or more of the jobs running on the machine have started more threads than their user requested cores, overloading the machine's resources.  
Being overloaded reduces the rate at which a computer completes work, because it has to load the state of each thread from RAM into a core, let the thread run for a while, and then save that state out to RAM, which adds overhead.  
To find out who is overloading a particular machine, you can run 'squeue -w _machinename_', which will list the jobs running on the machine, the partition that those jobs were sent to, and the user who started the job.  If the job(s) is/are from one of our partitions, ask the person responsible to address the problem.  If they're from one of the requeue partitions, send mail to RC and they'll fix it.


