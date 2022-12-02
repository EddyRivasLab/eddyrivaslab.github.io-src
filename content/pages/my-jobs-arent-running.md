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
'squeue -p _partitionname_  


