#!/usr/local/bin/python3

import sys
import collections

arg = sys.argv[1].lower()
stat = collections.defaultdict(int)

for ch in arg:
  stat[ch] += 1

for d, cnt in sorted(stat.items(), key = lambda entry: entry[1], reverse = True):
 print("{0} listed {1} times".format(d, cnt))
