from datetime import datetime

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

def sum_prime(z):
    '''
    Returns sum of prime numbers between 0 and z
    '''
    return sum([i for i in range(z) if is_prime(i)])

# Datetime module is used to time the script
start_time = datetime.now()

# Prints sum of prime numbers between 0 and 10**5 
print("Serial calculated sum of primes " + str(sum_prime(10**5)))

# Prints wall clock time
time_delta = datetime.now() - start_time
print("Elapsed wall clock time: " + str(time_delta) + "\n")
