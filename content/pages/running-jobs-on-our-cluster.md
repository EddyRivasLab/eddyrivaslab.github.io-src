Title: Running Jobs on Our RC Machines
Date: 11/29/22
Authors: Nick Carter
slug: running-jobs-on-our-cluster

The Research Computing cluster (Odyssey/Cannon) uses a tool called [Slurm](https://slurm.schedmd.com/) to manage jobs.  This page is not a tutorial on Slurm itself.  For that, see [Slurm's](https://slurm.schedmd.com/) webpage or Research Computing's [documentation](https://docs.rc.fas.harvard.edu/).

While Slurm works well in most cases, it has limitations, some fundamental, some due to how Research Computing has configured it on their resources, that mean that we need to take care when running large numbers of jobs to make sure that one person's jobs don't occupy all of our resources and prevent others from getting their work done. Among those limitations are:

1. _No Fairshare within groups_: [Fairshare](https://docs.rc.fas.harvard.edu/kb/fairshare/) is the system Slurm uses to decide which jobs to run when there are more jobs scheduled than a partition has resources.  The more a user or group has used the cluster recently, the higher their Fairshare score will be, which translates to their jobs having lower priority when Slurm decides which job to run next.  However, RC has turned off Fairshare for individual users, and is only using group-level Fairshare.  The result is that, for the machines we own, Fairshare does not exist, and jobs run in a first-in-first-out manner unless we do something to change that.

2. _No job eviction_: Once Slurm starts a job, on a partition other than one of the requeue partitions, that job will run to completion unless it uses more resources than the user requested. In general, this is a good thing, but it means that we need to take care when running jobs that take a long time to complete, as filling our cluster with long-running jobs can lock other users out for significant periods of time.

3. _Limited job scheduling horizon_: RC has configured Slurm such that it only examines the first 1500 jobs in the queue when selecting a job to run next.  This reduces the amount of time that Slurm taks to schedule a job, but means that large numbers of jobs from one user can block another user's job from running, even if the first user has niced their jobs to reduce their priority.

4. _No Limit on the number of cores/threads used_: While Slurm allows a user to request a number of cores for each job, it does not limit the number of threads or cores a job uses to the number requested.  When a job uses more cores/threads than the user requested, it can overload the machine, slowing work down and causing Slurm to put the machine in a "drng" state and not schedule additional jobs until the load goes down.

<h2>Running Jobs Without Hogging our Cluster</h2>
It's common in our lab for someone to want to run hundreds or thousands of jobs, so we've developed the following guidelines that allow one to submit large amounts of work at one time without preventing others from using the cluster.

1. Use job arrays whenever you submit more than 100 jobs at a time.  A job array can contain up to 10,000 tasks (independent jobs), but Slurm treats it as a single job for the purposes of scheduling, which makes it possible to schedule large amounts of work without filling up Slurm's 1500-job search range.  There are about 15 people in the Eddy and Rivas labs, so, if everyone follows this guideline, we should never fill up the job search range.  Job arrays also provide a convenient mechanism to limit the number of sub-jobs that run simultaneously.

2. Nice your jobs if running more than 200 jobs (15 people times 200 jobs is about equal to the number of cores in our partition).  Slurm provides a --nice option for both sbatch and srun, which changes the priority of a job or a job array.  The default nice value for jobs is 100, and higher nice values lower a job's priority, allowing less-nice jobs to pass them in the queue.  We don't have a specific policy on how much you should nice your jobs, but one suggestion is to use a nice value equal to the number of jobs you are running.

3. Limit the number of long-running (more than 1-2 hours) jobs you run at the same time.  Some of the jobs we run take days or weeks to complete, and filling up our resources with those jobs can lock others out of the cluster for long periods of time.  If you expect your jobs to run for more than 1-2 hours each, use either a job array's limit on the number of sub-jobs that can run simultaneously or the --exclude option to srun/sbatch to ensure that you aren't running more than 200 such jobs at a time.

4. Make sure that your jobs only use the number of cores you've requested from Slurm.  Most parallel programs have an option to specify the number of cores/CPUs they use, but the syntax of this varies from program to program.