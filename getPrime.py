import time

def getPrime(number:int):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def getPrimesCached(limit:int):
    primes = []

    for number in range(2, limit):
        isPrime = True
        for prime in primes:
            if number % prime == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(number)
    return primes

number = 0

amountOfPrimesToList = 50

for _ in range(amountOfPrimesToList):
    number += 1
    if getPrime(number):
        print(number)
        time.sleep(.5)


list_primes = getPrimesCached(amountOfPrimesToList)
for i in list_primes:
    print(i)
    time.sleep(.5)