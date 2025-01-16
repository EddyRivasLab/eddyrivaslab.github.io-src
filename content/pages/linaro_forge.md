Title: Using Linaro Forge on the RC Machines
Date: 1/16/25
Authors: Nick Carter
slug: linaro-forge

Linaro Forge is a debugger and performance-analysis tool that is mostly designed for multi-threaded and multi-machine (MPI) programs, but is also somewhat better than text-mode debuggers (in Nick's humble opinion) on sequential programs. I (Nick)
have only used it for C programs, but I believe it can be used for Python applications.

The debugger consists of two programs: A front-end that runs on your local machine (your laptop or desktop) and provides a GUI interface, and the debugger itself, which runs on a remote machine, such as one of the RC computers.  If your local machine is a Linux box, you can also run the debugger directly on it.

## Installing the Front-end

The first step in using Forge is setting up the front-end on your local machine.  Download the appropriate file for your machine https://www.linaroforge.com/download-documentation/ and follow the install instructions.  If your local machine is a Mac or Windows box, this will only install the front-end.  If your local machine runs Linux, this will install the full debugger, and you'll need a license file to tell the debugger how to contact the license server so that it can run.  Ask Nick C. for this, as it's not something we want publicly available.

Once you've installed the front-end, you're ready to connect to the debugger itself on one of the RC machines.

## Connecting to an RC Machine

In order to connect to an RC machine, you'll need a login session running on one of the -p eddy machines.  SSH to one of the RC login nodes, and use salloc to request a session on one of our machines.  Keep track of the particular machine you're running the session on.  You will also need to set up an SSH public-key/private-key pair on the RC systems so that you can SSH from one of the login nodes to one of our machines without entering a password.

Then, start the Linaro Forge front-end.  You'll get a window that has five options: run, attach, open core, manual launch, and remote launch.  Click the configure box under remote launch to set up the connection to the RC machine.  That will bring up another window with several fields.  The three you need to fill in are "Connection name", which can be anything you want, "Remote Installation Directory", which should be "/n/eddy_lab/software/linaro/forge/24.1", and "Host Name", which should be something like "rclogin.rc.fas.harvard.edu the-machine-you-have-a-session-on.rc.fas.harvard.edu".  (omit the quotation marks in all fields) You also need to click the "Proxy through login node" checkbox towards the bottom of the window.  All of this tells Forge that it needs to ssh to one of the RC login nodes and then from there to one of the 

Once you've done this, click the "test remote launch" button.  That will bring up another window.  Click the "show terminal" button and enter your RC password and two-factor authentication code.  The tool should then continue and give you a message that the test succeeded.  If it fails, check all the items in the Remote Launch Settings window, and pester Nick C. if you still have problems.

Now, you're ready to actually run the debugger.  Select the remote launch configuration you just created from the Remote Launch menu, and it should connect through and start Forge on the RC node.  Then, click "Run" to start the debugger, fill out the fields on the window that comes up appropriately, and you're ready to start debugging.

