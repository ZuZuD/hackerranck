#!/usr/bin/env python
import re
arg = input()
for i in range(arg):
    regex = raw_input()
    try:
        re.compile(regex)
        print 'True'
    except Exception:
        print 'False'
