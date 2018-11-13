#!/bin/bash
#SBATCH --partition=kamiak        ### Partition we want
#SBATCH --job-name=parallel_prime    ### Job Name
#SBATCH --output=parallel_prime_%J.out          ### File in which to store job output
#SBATCH --error=parallel_prime_%J.err         ### File in which to store job error messages
#SBATCH --time=0-00:05:00       ### Wall clock time limit for the job in Days-HH:MM:SS
#SBATCH --nodes=1               ### Number of nodes we want
#SBATCH --ntasks-per-node=1     ### Number of times to run our program on the node
#SBATCH --cpus-per-task=4		### Request 4 cores for our task

module load anaconda3  # Load the anaconda3 module

source activate env  # Activate the environment that we made

python parallel.py # Run the parallel python script

source deactivate # deactivate the environment
