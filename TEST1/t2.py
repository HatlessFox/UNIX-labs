#!/usr/local/bin/python3

import sys

arg = sys.argv[1]

def is_pol(st):
  return st == st[::-1]

def substr(st, code):
  res = [st[i] for i in range(len(st)) if code & 2**i == 0]
  return "".join(res)

max_p = ""
for code in range(0, 2**len(arg)):
  st = substr(arg, code)
  if is_pol(st) and len(st) > len(max_p):
    max_p = st

print(max_p)