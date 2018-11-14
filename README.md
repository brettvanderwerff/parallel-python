# parallel-python
Python code samples from the High Performance Computing with R and Python workshop, Presented by Brett Vanderwerff on 11/13/18

## Setup

To follow along with the guide, you will need an account on Kamiak, which can be requested at: https://wsu-its.atlassian.net/servicedesk/customer/portal/1/user/login?destination=portal%2F1

You also need to be able to log in to Kamiak. Info on logging in can be found here: https://hpc.wsu.edu/users-guide/terminal-ssh/ and

here: https://s3.wp.wsu.edu/uploads/sites/1122/2018/11/kamiak_cheat_sheet_v7.pdf

Once logged in, you will need to clone this repository into your home directory by entering the command

```commandline
$git clone https://github.com/wsucougpy/parallel-python
```
(Note: don't add the `$` for this command or any other command in this guide. The `$` prefix just denotes a shell command)

After cloning the repository, you should be able to use the `ls` command to see the repository 

```commandline
$ls
```
Which should output something similar to:

```commandline
[brett.vanderwerff@login-p1n02 ~]$ ls
parallel-python
[brett.vanderwerff@login-p1n02 ~]$
```
Once you have this repository, you are ready to start :)

## Creating a Conda Environment

We can request an idev session using the `idev` command, which takes us from the login node to a compute node

```commandline
$idev -t 30 
```

Load the `anadonda3` module

```commandline
$module load anaconda3
```

Check out the list of packages that are readily available without needing to set up an environment

```commandline
$conda list -n root
```

Create a conda environment named “env”

```commandline
$conda create -n env
```
(say yes when prompted)


Activate the environment “env”

```commandline
$source activate env
```

Install pip to “env”

```commandline
$conda install pip
```
(say yes when prompted)

Install a package from the Python Package Index to “env” (Note: this is just an example package)

```commandline
$pip install bitstring
```

Install a package from an anaconda repository to “env” (Note: this is just an example package)

```commandline
$conda install flask-sqlalchemy
```

(say yes when prompted)

Deactivate the “env” environment

```commandline
$source deactivate
```

Exit the idev session

```commandline
$exit
```


## Submitting a Python Job to SLURM (serial example)

Change into the `parallel-python` directory using the `cd` command.  Then use the  `ls` command to look at the files there

```commandline
$cd ~/parallel-python
```

```commandline
$ls
```

`serial.py` is a demo script that sums all the prime numbers between 0 and 10^5. We can see the contents of this file with the `cat` command

```commandline
$cat serial.py
```

`serial_job.sh` is a script for submitting `serial.py`  to `SLURM` (Kamiak’s job scheduler).  We can see the contents of this file with the `cat` command

```commandline
$cat serial_job.sh
```

`#!/bin/bash` is the “bang” line pointing  to the interpreter we want to use to run this file. 

The next few lines all start with #SBATCH and are recognized as arguments by SLURM:

* partition – the partition we want to run on
* job-name – the name of our job
* output – the file we want to write the standard output to
* error – the file we want to write standard error to
* time – the amount of “wall clock” time we want for the job
* nodes – the number of nodes we want to run the program on
* ntasks-per-node – the number of times we want to run the program on our node
* cpus-per-task – the number of cores for our program

The rest of the script gives commands to:

* load the `anaconda3` module
* activate the conda environment “env” that we made earlier
* use python to run the `serial.py` script
* deactivate the “env” environment
    

Submit the job to the job scheduler using the `sbatch` command

```commandline
$sbatch serial_job.sh
```
(when scheduled, it takes about 30 seconds to run) 

If the job is still running, we can check the progress using the `squeue` command (if the job already completed we won’t see anything here)

```commandline
$squeue -u your.name
```

When the job is complete we can use `ls` to see that an output file has appeared. We can see the contents of this file with the `cat` command

```commandline
$ls
```

```commandline
$cat serial_prime*.out
```

## Submitting a Python Job to SLURM (parallel example)

Change into the `parallel-python` directory using the `cd` command.  Then use the  `ls` command to look at the files there

```commandline
$cd ~/parallel-python
```
```commandline
$ls
```

`parallel.py`  is a script that sums all the prime numbers between 0 and 10^5 using a parallel approach with the multiprocessing module from Python’s standard library. We can see the contents of this file with the `cat` command

```commandline
$cat parallel.py
```

`parallel_job.sh` is a script for submitting `parallel.py`  to `SLURM` (Kamiak’s job scheduler).  We can see the contents of this file with the `cat` command. The only thing different between `parallel_job.sh` and `serial_job.sh` is that now we are asking for 4 cpus instead of 1

```commandline
$cat parallel_job.sh
```

Submit the job to the job scheduler using the `sbatch` command

```commandline
$sbatch parallel_job.sh
```
(when scheduled, it takes about 15 seconds to run)

Check out the results!

```commandline
$ls
```
```commandline
$cat parallel_prime*.out
```




