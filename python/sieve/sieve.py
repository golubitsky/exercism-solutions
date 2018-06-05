def sieve(limit):
    # is_prime: no off-by-one adjustment necessary
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False

    primes = []
    for i in range(2, limit + 1):
        if is_prime[i]:
            primes.append(i)
        j = i
        while True:
            j += i
            if j > limit:
                break
            is_prime[j] = False

    return primes
