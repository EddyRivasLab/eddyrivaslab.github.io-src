Title: My Jobs Aren't Running
Date: 11/28/22
Authors: Nick Carter
slug: my-jobs-arent-running
 
It's (sadly) fairly common for our RC machines to get into states where they aren't able to start new jobs.  Here are some ways to figure out what's going on if your jobs seem to be stuck in the queue

## Step 1: Check the state of the machines in the partition
The command 'sinfo -p _partitionname_' will generate a table showing the overall state of the machines in the partition.  The two most relevant fields in the table are the "AVAIL" and "STATE" fields.  "AVAIL" should always have the value "up".  If it doesn't, something has gone badly wrong; contact RC to get it looked at.  
The "STATE" field can have multiple values.  Each line in the table will have a different value in the "STATE" field, and the "NODELIST" field will list the machines in the partition that have that state.  The values you're likely to see in the "STATE" field are:  
*"alloc"  
Machines in the "alloc" state are fully-occupied with jobs from our group.  If there are jobs waiting for the partition, all of the machines should be in this state.  
*"mix"  
Machines in the "mix" state are some combination of idle, running our jobs, and running jobs from one of the "requeue" partition.  This state generally indicates that the machine(s) are healthy, and that there isn't enough work from our group to keep them full.  If machines stay in the "mix" state for a long time (more than 30 minutes) while our jobs are waiting, it may indicate a problem.  
*"up"  


