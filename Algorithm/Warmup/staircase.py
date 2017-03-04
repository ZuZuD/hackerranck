#!/usr/bin/env python
import sys

n = int(raw_input().strip())
for i in xrange(n):
  print ("#"*(i+1)).rjust(n,' ')
