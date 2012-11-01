#!/usr/local/bin/python3

import xml.etree.ElementTree as el_tree
import re

NAME_RE = re.compile("{.*}(.*)")

def print_(val, offset):
  tag_name = NAME_RE.search(val.tag).groups()[0]
  print("  "*offset + tag_name)
  for v in val:
    print_(v, offset+1)

root = el_tree.parse("top_songs_itunes.rss").getroot(); 
print_(root, 0)

