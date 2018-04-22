def ispal(a):
  if a == int(str(a)[::-1]):
    return True
  else:
    return False
def main():
  ref = []
  for a in range(99, 1000):
    for i in range(99, 1000):
      if ispal(a*i) == True:
        ref.append(a*i)
  return max(ref)
print(main())
