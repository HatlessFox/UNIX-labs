#!/usr/local/bin/python3

def gen_perms(n):
  curr = [i for i in range(1, n+1)]
  yield curr