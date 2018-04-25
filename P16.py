def main():
  n = 2**1000
  c = 0
  for i in list(str(n)):
    c += int(i)
  return c
print(main())
