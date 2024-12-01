numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
print(len(numbers))
for i in range(len(numbers)):
    if i == 1:
        continue
    elif i % 2 == 0:
        not_primes.append(i)
    else:
        primes.append(i)
print(primes)
print(not_primes)
