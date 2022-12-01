Title: Using Job Arrays
Date: 12/1/22
Authors: Nick Carter
slug: using-job-arrays

Slurm job arrays are the preferred way to run large numbers of jobs on the RC cluster because Slurm's scheduler sees a job array as a single item when deciding what job to run next.  That makes job arrays a convenient way to submit large numbers of jobs<span class="marginnote">Up to 10,000 on the RC cluster.</span> to the scheduling queue without filling up the 1,500-task window that Slurm examines when selecting the next job to run and blocking other users' jobs from running.

##Submitting a job array  
Slurm uses the syntax "--array=range", where "range" specifies the IDs of the sub-jobs within the array, to indicate that a job array is being submitted.  This can either be passed as an option to srun or as one of the header lines in an sbatch script: "\#SBATCH --array=range".  
The range of a job array can either be specified by its start and end IDs, e.g. "--array=1-1000" or as a list of IDs such as "--array=1,3,5,7".  You can also specify a stride in the range, so "--array=1-1001:2" would create an array of 500 sub-jobs whose IDs are the odd numbers from 1 to 1001.

###Limiting the number of sub-jobs that run simultaneously
Adding "%joblimit" to the end of an array specification will limit the number of sub-jobs from the array that Slurm will run at one time, so the specification "--array=1-10000:100" creates an array of 10,000 jobs but tels Slurm to run at most 100 of them at a time.   Use of this option is very strongly recommended if the sub-jobs within your array take more than an hour or two to run to avoid locking others out of the cluster.

##Using job IDs
Slurm assigns each sub-job within an array a numeric ID that is its position within the range specified for the array.  When running a job array, you need to use these IDs to make each sub-job do something different, or you'll wind up running many copies of the same job.  
Within an sbatch script that specifies a job array, Slurm defines two variables: %A contains Slurm's ID for the entire job array, and %a contains the ID of the sub-job within the array.  One use for these variables is to create distinct output and error files for each sub-job.  For example, putting the lines "\#SBATCH -o hmmer_test.%A.%a.out" and "\#SBATCH -e hmmer_test.%A.%a.err" in an sbatch script will create unique output and error files for each sub-job in the script even if the script is run many times, unless the Slurm job IDs roll over and repeat themselves, which happens infrequently on the RC cluster.  

###Accessing job IDs within a sub-job
Slurm defines a SLURM_ARRAY_TASK_ID environment variable for each sub-job in an array, which will have the same value as the %a variable in the sbatch script.  If each sub-job is itself a shell script, you can access this environment variable with $SLURM_ARRAY_TASK_ID.  If your sub-jobs are Python scripts, the lines "import sys" followed by Jobid = sys.getenv\(‘SLURM_ARRAY_TASK_ID’\) will get the value of the environment variable.  In R, "Task_id <- Sys.getenv\(“SLURM_ARRAY_TASK_ID”\)" will fetch the variable's value.

###Using array ID's to select input files from directories
It's common in our lab for someone to have a directory of input files that they want to run the same program on, but there's often no obvious way to map job IDs to different files in a directory.  The [University of Florida's Research Computing](https://help.rc.ufl.edu/doc/SLURM_Job_Arrays) documentation on job arrays provides a way to do this.  In an sbatch file, the line "file=\$\(ls /path/to/directory/* | sed -n \$\{SLURM_ARRAY_TASK_ID\}p\)" 



