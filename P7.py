import random
def miller_rabin(n):
      k = 10
      if n == 2:
              return True
      if n % 2 == 0:
              return False
      r, s = 0, n - 1
      while s % 2 == 0:
            r += 1
            s //= 2
      for _ in range(k):
            a = random.randint(2, n - 1)
            x = pow(a, s, n)
            if x == 1 or x == n - 1:
                  continue
            for _ in range(r - 1):
                  x = pow(x, 2, n)
                  if x == n - 1:
                        break
            else:
                    return False
      return True
def main():
  count = 0
  a = 1
  primes = [2]
  while count != 10001:
    a += 2
    if miller_rabin(a) == True:
      primes.append(a)
      count += 1
    if count == 10001:
      return primes[10000]
print(main())
