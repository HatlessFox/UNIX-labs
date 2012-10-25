#!/usr/local/bin/python3

import math

def is_product_of_K_primes(n, k = 2):
  bound = math.floor(math.sqrt(n)) + 1
  divs = []
  
  for i in range(2, bound):
    while n % i == 0:
      divs.append(i)
      n //= i
    if n == 1: break
    if len(divs) > k: return False

  if n != 1: divs.append(n)
  return len(divs) == k;  

n = int(input("Enter N: "));

data = [i for i in range(4, n) if is_product_of_K_primes(i)];
for d in data: print(d)
if len(data) == 0: print("No solution")

