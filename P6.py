def sum_diff_square(max):
  c = 0
  for a in range(1, max+1):
    c += a
  c = c**2
  count = 0
  for a in range(1, max+1):
    count += a**2
  return c - count
print(sum_diff_sqaure(100))
