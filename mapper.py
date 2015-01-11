#!/usr/bin/python

import sys
import string

for line in sys.stdin:
  line = line.strip()
  words = line.split()

  for word in words:
    word = word.translate(string.maketrans("",""), string.punctuation)
    word = word.lower()
    print '%s\t%s' % (word, 1)