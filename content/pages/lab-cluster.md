Title: Eddy and Rivas Lab Cluster Resources and how to Access Them
Date: 11/16/22
slug:cluster-computing-in-the-eddy-and-rivas-labs
Authors: Sean Eddy

Our high performance cluster computing is managed by
[Harvard Research Computing](https://www.rc.fas.harvard.edu/) (RC).


## Overview 

Your RC _home directory_ is something like `/n/home01/<username>`.
When you log in, that's where you'll land. You have 100GB of space
here. 

Our _lab storage_ is `/n/eddy_lab/`. We have 400TB of what RC calls
Tier 1 storage, which is fast but expensive. 

Both your home directory and our lab storage are backed up nightly to
what RC calls _snapshots_, and periodically to what RC calls _disaster
recovery_ (DR) backups.

It's convenient to be able to browse and edit your files on the
cluster directly from your laptop or desktop without logging into the
cluster. If you get on the RC VPN, you can remote mount your home
directory and/or the `/n/eddy_lab` lab filesystem on your local
machine using `samba`. (Warning: a samba mount is slow, and may
sometimes be flaky; don't rely on it except for lightweight tasks.)
Instructions are below.

RC also provides _shared scratch storage_, which is very fast but not backed up.  Files on the scratch storage that are older than 90 days are automatically deleted, and RC strongly frowns on playing tricks to make files look younger than they are.  Because RC occasionally moves the scratch storage to different devices, the easiest way to access it is through the $SCRATCH variable, which is defined on all RC machines.  Our lab has an eddy_lab directory on the scratch space with a 50TB quota, which contains a Users directory, so '$SCRATCH/eddy_lab/Users/<yourusername>' will point to your directory on the scratch space <span class="marginnote">The Users directory was pre-populated with space for a set of usernames at some point in the past.  If your username wasn't included, you'll have to email RC to get a directory created for you.</span>.  

The scratch space is intended for temporary data, so is a great place to put input or output files from jobs, particularly if you intend to post-process your outputs to extract a smaller amount of data from them.

You can read
[more documentation on how RC storage works](https://docs.rc.fas.harvard.edu/kb/cluster-storage/).

All of our lab's computing equipment is contained in the eddy partition, which contains 1,872 cores.  Most of our machines have 8GB of RAM per core.  In addition, we have three GPU-equipped machines, which are part of the partition: holygpu2c0923, holygpu2c1121, and holygpu7c0920<span class="marginnote">The "holy" at the beginning of our machine names refers to their location in the Holyoke data center.</span>

  Each holygpu2c node has 8 [NVIDIA Ampere A40 GPUs](https://www.nvidia.com/en-us/data-center/a40/)
  with 48G VRAM [installed 2022].  
  
  The holygpu7 node has 4 [NVIDIA HGX A100 GPUs](https://www.nvidia.com/en-us/data-center/hgx/)
  with 80G VRAM [installed 2023].  
  
We can also use Harvard-wide shared partitions on the RC cluster. `-p
shared` is 19,104 cores (in 399 nodes), for example (as of Jan 2023). RC has
[much more documentation on available partitions](https://docs.rc.fas.harvard.edu/kb/running-jobs/#Slurm_partitions).


## Accessing the cluster

### logging on, first time

* Get a [Research Computing (RC) account](https://rc.fas.harvard.edu/resources/faq/how-do-i-get-a-research-computing-account/).
* Read about how to [access the RC cluster](https://docs.rc.fas.harvard.edu/kb/access-and-login/)
* Install [OpenAuth two-factor authentication](https://docs.rc.fas.harvard.edu/kb/openauth/)

* Behold the glory of
  [RC's extensive documentation](https://docs.rc.fas.harvard.edu/),
  where most questions you have about RC are answered.

* If you chose to install their little Java OpenAuth application on your
  machine to generate your OpenAuth codes (instead of using Duo Mobile
  or Google Authenticator on your smart phone), it's convenient to
  make an alias for launching it. In my `.bashrc`, I have `alias
  ody-auth='~/sw/seddy-openauth/seddy-openauth.sh &'`, so I can launch
  my authenticator on the commandline with `ody-auth`.

You should be able to ssh into the cluster now. With your username in
place of mine (`seddy`), do:

```
    % ssh seddy@login.rc.fas.harvard.edu
```

It'll ask for your RC password and an OpenAuth two-factor
authentication key.



### configuring an ssh host alias 

Once you're using the cluster a lot, you can save yourself some typing
by setting up a host alias. Mine is called **ody**, because the RC
cluster used to be called Odyssey.  Add something like this to your
`.ssh/config` file, using your preferred host alias in place of `ody`
and your username in place of `seddy`:
  
```bash
Host                  ody
  HostName            login.rc.fas.harvard.edu
  User                seddy
  Compression         yes
  ForwardX11Trusted   yes
  ServerAliveInterval 30
```

Now you can access RC just by:

```
    % ssh ody
```

You still have to authenticate by password and OpenAuth code, though.

	
### configuring single sign-on scp access

Even better, but a little more complicated: you can make it so you
only have to authenticate once, and every ssh or scp after that is
passwordless. To do this, I use
[SSH ControlMaster for single sign-on](https://docs.rc.fas.harvard.edu/kb/using-ssh-controlmaster-for-single-sign-on/),
to open a single `ssh` connection that you authenticate once, and all
subsequent `ssh`-based traffic to RC goes via that connection.

RC's
[instructions are here](https://docs.rc.fas.harvard.edu/kb/using-ssh-controlmaster-for-single-sign-on/)
but briefly:

* Replace the above hostname alias in `.ssh/config` file with
  something like this:
  
```bash
Host              ody
   User           seddy
   HostName       login.rc.fas.harvard.edu
   ControlMaster  auto
   ControlPath    ~/.ssh/%r@%h:%p
   ControlPersist yes
```

* Add some aliases to your `.bashrc` file:

```bash
   alias ody-start='ssh -Y -o ServerAliveInterval=30 -fN ody'   
   alias ody-stop='ssh -O stop ody'
   alias ody-kill='ssh -O exit ody'
```

Now you can launch a session with:

```
    % ody-start
```

It'll ask you to authenticate. After you do this, all your ssh-based
commands (in any terminal window) will work without further
authentication. To stop the connection, do

```
    % ody-stop
```

If you forget to stop it, no big deal, the connection will eventually
time out by itself.



________________________________________________________________

## Accessing our storage


### set up VPN access

You don't need to be on the RC VPN to log in to the cluster, but you do
need to be on the VPN if you want to mount any of our RC storage on
your local machine.

* Set up [VPN access to Odyssey](https://rc.fas.harvard.edu/resources/vpn-setup/).


### mounting our lab filesystem on your machine

You need to be on the RC VPN to remote mount our filesystem.

From the Mac OS/X Finder, choose Go->Connect To Server, and give it:
```bash
   smb://eddyfs.rc.fas.harvard.edu/eddy_lab
```

It will mount at `/Volumes/eddy_lab` on your local machine, and it
will show up in Locations in the Finder. 

If your username on your local machine is different from your username
on the cluster, make that URL `smb://<username>:eddyfs.rc.fas.harvard.edu/eddy_lab`.

To use the OS/X command line instead of the Finder GUI:
```bash
   # to mount:
   % osascript -e 'mount volume "smb://eddyfs.rc.fas.harvard.edu/eddy_lab`
   # to unmount:
   $ umount /Volumes/eddy_lab
```

You can also samba-mount your cluster home directory [[RC
documentation is
here](https://docs.rc.fas.harvard.edu/kb/mounting-storage/)]. Figure
out where your home dir is (`cd; pwd`). It's something like
`/n/homeXX/<username>`; mine is `/n/home14/seddy`. The URL to samba
mount my home dir is
`smb://rcstore.rc.fas.harvard.edu/homes/home14/seddy`. Replace those
last two bits with your own `homeXX/<username>`.

I have these aliased in my `.bashrc`:

```
    alias ody-mount="osascript -e 'mount volume \"smb://eddyfs.rc.fas.harvard.edu/eddy_lab\"'"
    alias ody-home-mount="osascript -e 'mount volume \"smb://rcstore.rc.fas.harvard.edu/homes/home14/seddy\"'"
    alias ody-umount='umount /Volumes/eddy_lab'
    alias ody-home-umount='umount /Volumes/seddy'
```

All reputable people say it's important to remember to unmount the
filesystem before you do something that breaks the network connection
(like logging out of the VPN). On the other hand, I routinely forget,
and nothing has imploded yet.

________________________________________________________________

## Accessing our shared data (genomes, seq db's)

Many standard sequence databases are installed in
`/n/eddy_lab/data/` including
Pfam, Rfam, and UniProt.

Many genome and transcriptome datasets are installed in
`/n/eddy_lab/genomes/`.

________________________________________________________________

## Working on the cluster

RC has a zillion software packages installed and available, but most
are not in your `${PATH}` by default. You load an available package
with the `module` command. For example, `module load hmmer` loads RC's
current installed version of HMMER, and `module load blast` loads
BLAST. `module avail` lets you behold (almost) everything available,
though it takes a while to run.

You generally work on RC using the SLURM batch scheduler either to
obtain interactive command-line access to a compute node, or to
schedule jobs to run on compute nodes. You shouldn't do any
substantial computation on login nodes. The `sbatch` command submits
batch scripts to SLURM for later execution.  The `srun` command runs a
single command on our compute resources interactively.  The `sbatch
--wrap="<cmd>"` option submits a single command into the batch queue,
and is the most common way that I send jobs to the cluster.

The notes below give useful `module` and SLURM incantations without a
ton of explication. More thorough RC documentation to skim includes:

* [Using modules](https://docs.rc.fas.harvard.edu/kb/modules-intro/)
* [Cluster Quick Start Guide](https://docs.rc.fas.harvard.edu/kb/quickstart-guide/)
* [Running Jobs (with SLURM)](https://docs.rc.fas.harvard.edu/kb/running-jobs/)


### the module command; compiling software 

It's ok to compile on a login node (but that's about it). My usual
pre-incantation before working on development of our software (HMMER,
Infernal, Easel):

``` 
	module load gcc git valgrind python
```

This loads the `gcc` compiler, an up-to-date version of `git`, the
`valgrind` memory debugging tools, and Python3 (the default python on
RC is Python2).

Other `module` command examples:

```
	module load intel        # Intel icc compiler instead
	module load gcc openmpi  # for MPI parallel software, usually I use gcc/OpenMPI

	module avail             # show list of immediately available modules
	module avail openmpi     # show list of available openmpi modules (there may be different versions installed)
    module list              # list my currently loaded modules
	module unload gcc        # unload a module
	module swap intel gcc    # swap one module out (intel icc) for another (gcc)
    module purge             # unload all modules

	module load gcc/7.1.0-fasrc01 binutils/2.29-fasrc01   # sometimes we need to be very specific about versions
```


### get an interactive cpu node

Depends on whether you just need a single cpu core (most common),
several cores (for multithreaded software like BLAST or HMMER), or an
entire compute node (40 cores, for the nodes in our `-p eddy`
partition). My standard incantations are:

```
	srun -p eddy --pty -t 6-00:00 /bin/bash                      # 1 core
	srun -p eddy --pty -t 6-00:00 -c 8 /bin/bash                 # multiple cores; here 8
	srun -p eddy --pty -t 6-00:00 -c 40 --exclusive /bin/bash    # entire node
```

* `-p eddy` says you want one of the nodes in our main cpu partition. 
* `--pty` says you want an interactive terminal.
* `-t 6-00:00` says you want it assigned to you for up to 6
  days. You're not going to use it that long - you're going to log out
  when you're done (right?), but RC needs you to specify an estimated
  time.
* `-c 8` or `-c 40` says you want to use 8 or 40 cores (or whatever). All the machines in
  the `-p eddy` partition have 40 cores. I think if you don't specify
  this, even if you get exclusive access to the node, you may only be
  able to use 1 core on it.
* `--exclusive` says that no other job will be allowed to start on
  your node while you're using it.
  
  
### run one command 

The most common way I submit tasks to the cluster is one command at a
time.  The `--wrap` option to `sbatch` lets you submit a job without
having to write a SLURM script for it.

```
    sbatch -t 6-00:00 -p eddy -c 4 -N 1 --wrap="hmmsearch --cpu 4 fn3.hmm /n/eddyfs01/data/dbs/Uniprot/uniprot_sprot.fasta"
```

`hmmsearch` is multithreaded; I'm matching the number of cores I
request from SLURM (`-c 4`) to the number of cores I'm telling
hmmsearch to use (`--cpu 4`), and telling SLURM I want them all on one
compute node (`-N 1`). For a non-parallel program, you'd leave off the
`-c 4` in the `sbatch` options.

The stdout goes to a SLURM outfile, something like
`slurm-56384497.out`. Or you can add a shell redirect `> foo.out` to
your `--wrap` command if you like.


### running a few commands, looping over some input files 

A couple of examples of ways to submit several commands at once:

```
    ls *.gz | xargs -I {}  sbatch --wrap="gunzip -c {}"   # uncompress all .gz files in this directory

    for FILE in *.fa; do
      echo ${FILE}
      sbatch -p eddy -t 10 --wrap="gzip ${FILE}"          # compress all .fa files in this directory
      sleep 1                                             # pausing between submissions to be kind to the scheduler
    done
```


### writing an sbatch script

If your job is more complicated than a single command - for example,
if it depends on loading software with a `module load` command first -
you can write an `sbatch` script. The SLURM options go into the
script, instead of on the `sbatch` command line, using a special
format. An example that (stupidly) loads gcc and just calls
`hostname`, so the output will be the name of the compute node the
script ran on:

```
#!/bin/bash
#SBATCH -c 1 	 	# Number of cores/threads
#SBATCH -N 1 	 	# Ensure that all cores are on one machine
#SBATCH -t 6-00:00 	# Runtime in D-HH:MM
#SBATCH -p eddy		# Partition to submit to
#SBATCH --mem=4000 	# Memory pool for all cores (see also --mem-per-cpu)
#SBATCH -o myjob_%j.out 	# File to which STDOUT will be written; %j is the job number assigned by SLURM
#SBATCH -e myjob_%j.err 	# File to which STDERR will be written

module load gcc
hostname
```

Save this to a file (`foo.sh` for example) and submit it with `sbatch`:

```
    sbatch foo.sh
```


### running lots of commands

If you have to submit lots of jobs (hundreds or thousands) to the
cluster at once, the preferred way to do it is with **job arrays**, to
avoid overloading the scheduler. See the
[RC documentation](https://docs.rc.fas.harvard.edu/kb/running-jobs/#Job_arrays).


### monitoring your running jobs

The `sinfo` command shows information about what's currently running where.

```
    sinfo -p eddy    # show the state of the `eddy` partition
	sinfo -a         # show the state of all RC partitions
```

The `sacct` command shows SLURM log info about jobs you ran in the past.

```
	sacct                                                      # default log
	sacct --format=jobid,jobname,state,cputime,elapsed,maxrss  # custom-formatted to get cputime (`cputime`), max mem (`maxrss`) used
	sacct --name=B1n-2.sh 	                                   # --name=<jobname> to see a particular job
    sacct -S 2020-03-29                                        # see jobs you started on 3/29/2020
```


### etiquette

We have two partitions, `-p eddy` with 640 cores and 4.8GB RAM/core
and `-p eddy_hmmer` with 576 slower cores and 3.7GB/core.  We often
use `-p eddy` for daily work (where we want stuff to be
near-interactive, finishing in minutes not hours). If you submit 600+
long-running jobs to `-p eddy`, nobody else can use it for a while.
To avoid getting in each others' way on `-p eddy`, at any one time,
please limit your resource use to:

  * <50% of the cores (320)
  * <50% of the RAM per node (96G) OR <4.8GB/core
  * <30min per job

Larger workloads can be sent to the `-p eddy_hmmer` queue, our night
train, without any etiquette on job number, memory piggishness, or
time.

The <320 core, <96G/node|<4.8G/core memory, <30min guidelines are just
guidelines.  The principle is what's important.  Nobody should have to
wait >30min to get their job to start running on `-p eddy`. If you
cause such pain, there may be public shaming and/or donut penalty.
Launching one job that takes a day to complete, or a thousand
10-second jobs is not going to get in anyone's way either. Conversely,
it's possible that three or more people in the lab could try to occupy
50% of our resources at a time and jam us up, so use `sinfo -p eddy`
to see how busy things are and be reasonable.

You can also add `--nice 1000` to your `sbatch` command, to downgrade
your running priority in the queue, which helps let other people's
jobs get run before yours.

