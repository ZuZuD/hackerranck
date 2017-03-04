#!/usr/bin/env python
import sys
import re

s = raw_input()
print(len(re.findall('[a-zA-Z][^A-Z]*',s)))
