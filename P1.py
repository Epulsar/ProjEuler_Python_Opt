def main():
  c = 0
  for a in range(2, 1000):
    if a%3 == 0 or a%5 == 0:
      c += a
  return c
print(main())
