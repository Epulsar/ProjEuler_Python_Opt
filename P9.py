def main():
  for a in range(1, 1000):
    for b in range(1, 1000):
      for c in range(1, 1000):
        if c**2 == a**2 + b**2:
          if a + b + c == 1000:
            return a * b * c
print(main())
