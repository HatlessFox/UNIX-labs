#!/usr/bin/python
#coding=UTF-8
from pymorphy import get_morph
import sys
import re
import unicodedata

PATH_TO_DICT = "ru"

morph = get_morph(PATH_TO_DICT)

def count_rus_nouns(file_name):
  nouns = set()
  total = 0
  noun_class = morph.get_graminfo(unicode("СОБАКА","UTF-8"))[0]['class'];
  book = open(file_name)
  for line in book:
    for word in re.split(r'[,.: ?!]', line):
      for w_info in morph.get_graminfo(unicode(word, "UTF-8").upper()):
        if w_info['class'] == noun_class:
          nouns.add(w_info['norm']);
          total += 1
          break
  book.close()
  return (len(nouns), total)


if __name__ == "__main__":
  unique, total = count_rus_nouns(sys.argv[1]);
  print "Total nouns:", total
  print "Different nounts:", unique