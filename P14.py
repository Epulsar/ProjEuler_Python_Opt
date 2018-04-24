def Collatz(start):
  len = 0
  while start != 1:
    if start%2 == 0:
      start = int(start/2)
      len += 1
    if start == 1:
      return len + 1
    if start%2 != 0:
      start = (3*start) + 1
      len += 1
    if start == 1:
      return len + 1
def main():
  chain = []
  for a in range(2, 1000000):
    chain.append([Collatz(a), a])
  return max(chain)
print(main())
