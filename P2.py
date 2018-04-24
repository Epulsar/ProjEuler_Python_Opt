def Fibonacci(max):
  list = [1, 2]
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
  ref = 0
  even = [2]
  count = 0
  while ref < 4000000:
    count += 1
    ref = Fibonacci(count)
    if ref%2 == 0:
      even.append(ref)
  adder = 0
  for i in even:
    adder += i
  return adder
print(main())
