Title: My Jobs Aren't Running
Date: 11/28/22
Authors: Nick Carter
slug: my-jobs-arent-running
 
It's (sadly) fairly common for our RC machines to get into states where they aren't able to start new jobs.  Here are some ways to figure out what's going on if your jobs seem to be stuck in the queue

## Step 1: Check the state of the machines in the partition
The command 'sinfo -p _partitionname_' will generate a table showing the overall state of the machines in the partition.  Each line in the table shows the state of a set of machines in the partition (each line includes all the machines in a particular state).  
The two most relevant fields in the table are the "AVAIL" and "STATE" fields.  "AVAIL" should always have the value "up".  If it doesn't, something has gone badly wrong; contact RC to get it looked at.  
 

