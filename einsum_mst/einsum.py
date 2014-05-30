import numpy as np
from collections import OrderedDict

def combo(n):
  r = [0] * len(n)
  while True:
    yield tuple(r)
    p = len(r) - 1
    r[p] += 1
    while r[p] == n[p]:
      r[p] = 0
      p -= 1
      if p == -1:
        return
      r[p] += 1

def einsum(str, *operands):
  pass

def string_mapping(str):
  temp = str.split('->')
  temp2 = temp[0].replace(',', '')
  distinct_letters = ''.join(OrderedDict.fromkeys(temp2[0]).keys())
  return distinct_letters