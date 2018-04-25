def Fibonacci(max):
  list = [1, 1]
  a = 0
  b = 1
  term = 0
  for i in range(0, max-2):
    term = list[a] + list[b]
    list.append(term)
    a += 1
    b += 1
  return term
def main():
  ref = 1
  c = 2
  while len(str(ref)) != 1000:
    ref = Fibonacci(c)
    c += 1
    if len(str(ref)) == 1000:
      return c - 1
print(main())
