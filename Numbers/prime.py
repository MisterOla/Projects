import math
 
def prime(n):
    i = 2
    while i < 0.5 + math.sqrt(n):
      if n % i == 0:
        return False
      i+=1
    return True
 
def primefactors(n):
    factors = []
    for i in range(n/2, 0, -1):
      if prime(i) and n % i == 0:
        factors.append(i)
    return factors

# driver code
print primefactors(9)   == [3, 1]
print primefactors(21)  == [7, 3, 1]
print primefactors(156) == [13, 3, 2, 1]
