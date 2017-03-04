#!/usr/bin/env python
from datetime import date
tab = raw_input().split()
d = date(int(tab[2]), int(tab[0]), int(tab[1]))
print d.strftime("%A").upper()
