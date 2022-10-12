"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):

    if (number_of_primes <= 0) :
        raise ValueError("number_of_primes must be above 0")


    list = []
    num = 1

    while (len(list) < number_of_primes):

        num+=1
        prime = True

        for n in range(num):

            if ((n > 1) and ((num % n) == 0)):
                prime = False
                break
        
        if prime:
            list.append(num)

    return list
