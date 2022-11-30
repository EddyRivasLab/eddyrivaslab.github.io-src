Title: Modifying This Website
Date: 11/28/22
Authors: Nick Carter
slug: modifying-this-website

This website is built using [Github Pages](https://pages.github.com/) and  [Pelican](https://getpelican.com/), a tool that converts documents written in Markdown into HTML websites.  All of the complexity of running Pelican and getting the resulting web pages into the right place for Github to serve them as a website has been automated, so after some first-time setup, making changes only requires a Git checkout-commit-push cycle.

##First time Setup
1. _Get access to the Github repositories_: Ask Sean to give you write (push) access to the eddyrivaslab.github.io and eddyrivaslab.github.io-src repositories on the EddyRivasLab Github project.  This will require that you create an account on www.github.com and give Sean your account name so that he can give you the permissions you need.

2. _Set up your work environment_:
The simplest way to contribute to this site is to do your work on the RC cluster, where all of the required Pelican and Python packages have already been installed. To do that, add the lines "export PATH=\$PATH:/n/eddy_lab/software/bin" and 
"export PYTHONPATH=$PYTHONPATH:/n/eddy_lab/software/python-packages" to the .bashrc file in your home directory. <span class="marginnote">If you've used the export HOME=/n/eddy_lab?users/username trick to make it look like your directory in our lab disk space is your home directory, you'll need to find your actual /n/homeXX/username home directory and make the changes to the .bashrc file in that directory.</span> After you've done that, log out of the cluster and back in again, and everything should be set up for you to use Pelican and our other local software installs.

If you want to work on your laptop or other local machine, you'll have to set up Python on that machine and then install Pelican from getpelican.com.  You'll then have to install the (list goes here when I have my notes) Python packages using pip. 

4. _Set up a Github SSH key_:  If you haven't already done so, follow the instructions at "https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account" to add an SSH key to your Github account.  This will allow the different git push operations required to modify the website to run without you having to enter username/password information.

5. _Clone the source repository_: Run "git clone git@github.com:EddyRivasLab/eddyrivaslab.github.io-src.git" to clone a copy of the source repository into your local filesystem.  You do not need to clone the eddyrivaslab.github.io repository: all work on that repository is done automatically when you run a "git commit" operation.

##Modifying the Site
Once you've done the first-time setup, making changes to this website is fairly simple:

1. _Make sure you have the most recent version_: Cd into the directory where you cloned the eddyrivaslab.github.io-src repository and run "git pull", which will update your local copy with any changes that have been made since your last pull.

2. _Make your changes_: The markdown pages containing our guides are located in the content/pages subdirectory of the git repository.  If you just want to modify an existing guide, all you need to do is edit the corresponding file.

To create a new guide, copy the "template.md" file from the top-level directory to content/pages/yourfilename.md and run "git add content/pages/yourfilename.md" so that Git will know that the file has been added to the repository, and then edit that file.  At the top of the markdown file you'll find four lines that start with "Title:", "Date:", "Authors:" and "slug:" that are used by Pelican to configure the resulting web page.  You'll need to edit those.  Most of them should be self-explanatory, except for the "slug:" field.  Pelican uses that field to create the names of files associated with your guide, so it needs to be something that will be a legal filename on UNIX, Mac, and Windows computers.

  One useful convention is to make the slug for a page the title of the page with all text in lowercase, spaces replaced by dashes and all other punctuation removed, so a page titled "Nick's Amazing Guide" would have the slug "nicks-amazing-guide".  If you use the same convention for naming your markdown files, it'll be easy for others to figure out which file contains the source for each guide.

After you've modified the Pelican lines, go ahead and write your page in Markdown.  One note: the template we use to format our website will insert a title containing the value in the "Title:" field at the top of your page, so there's no need to put a top-level title in the markdown file.

3. _Commit and Push_: 