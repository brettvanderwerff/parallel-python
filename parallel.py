from datetime import datetime
import multiprocessing as mp

def is_prime(n):
    '''
    Returns True if n is prime, else returns False.
    '''
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def worker(a,z):
    '''
    Returns sum of prime numbers between a and z
    '''
    return sum([i for i in range(a,z) if is_prime(i)])

def part_count(n, core_count):
    '''
    Make nested args list for worker functions:
    [[a,z], [a,z], …]

    i.e [[0, 500], [500, 1000]] where n=1000, core_count = 2
    '''
    step = int(n / core_count)
    part_count = [[step * x, step * x + step]for x in range(core_count)]
    part_count[-1][-1] += n % core_count
    return part_count

if __name__ == '__main__':
    
    #Datetime module is used to time the script
    start_time = datetime.now()

    #Specify that we have 4 cores and want to sum prime numbers up to 10**5
    inputs = part_count(n=10**5, core_count=4)

    #Pool object represents a pool of workers equal to the number of cores
    #starpmap method triggers 4 worker functions to begin processing their subset of the data
    p = mp.Pool(processes=4)
    results = p.starmap(func=worker, iterable=inputs)

    # Prints sum of prime numbers and wall clock time
    print("Parallel calculated sum of primes " + str(sum(results)))
    time_delta = datetime.now() - start_time
    print("Elapsed wall clock time: " + str(time_delta) + "\n")






