from fractions import gcd
def main():
  numbs = []
  for a in range(1, 20):
    numbs.append(a)
  lcm = numbs[0]
  for i in numbs[1:]:
    lcm = int(lcm*i/gcd(i, lcm))
  return lcm
print(main())
