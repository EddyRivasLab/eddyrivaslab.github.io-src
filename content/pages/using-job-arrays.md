Title: Using Job Arrays
Date: 12/1/22
Authors: Nick Carter
slug: using-job-arrays

Slurm job arrays are the preferred way to run large numbers of jobs on the RC cluster because Slurm's scheduler sees a job array as a single item when deciding what job to run next.  That makes job arrays a convenient way to submit large numbers of jobs<span class="marginnote">Up to 10,000 on the RC cluster.</span> to the scheduling queue without filling up the 1,500-task window that Slurm examines when selecting the next job to run and blocking other users' jobs from running.

##Submitting a job array  
Slurm uses the syntax "--array=range", where "range" specifies the indices of the sub-jobs within the array, to indicate that a job array is being submitted.  This can either be passed as an option to srun or as one of the header lines in an sbatch script: "\#SBATCH --array=range".  
The range of a job array can either be specified by its start and end indices, e.g. "--array=1-1000" or as a list of indices such as "--array=1,3,5,7".  You can also specify a stride in the range, so "--array=1-1001:2" would create an array of 500 sub-jobs whose indices are the odd numbers from 1 to 1001.

###Limiting the number of sub-jobs that run simultaneously
Adding "%joblimit" to the end of an array specification will limit the number of sub-jobs from the array that Slurm will run at one time, so the specification "--array=1-10000:100" creates an array of 10,000 jobs but tels Slurm to run at most 100 of them at a time.   Use of this option is very strongly recommended if the sub-jobs within your array take more than an hour or two to run to avoid locking others out of the cluster.



