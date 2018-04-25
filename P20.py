from decimal import *
getcontext().prec = 1000
import math
def main():
  n = Decimal(math.factorial(100))
  c = 0
  for i in list(str(n)):
    c += int(i)
  return c
print(main())
