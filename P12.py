def sum(upper):
    count = 0
    for a in range(1, upper+1):
        count += a
    return count
def factor(n):
    out = []
    for i in range(1, n + 1):
        if n % i == 0:
            out.append(i)
    return out
c = False
count = 1
while c != True:
    count += 1
    triangle = sum(count)
    factors = factor(triangle)
    #print(triangle, factors)
    if len(factors) > 500:
        c = True
        print(triangle)
