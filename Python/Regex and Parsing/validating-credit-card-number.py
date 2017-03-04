#!/usr/bin/env python
import re

reg = re.compile(r'^[4-6]([0-9]){15}')
reg_not = re.compile(r'.*(.)\1{3,}')
length = input()
tab = [raw_input() for j in range(length)]
tab_bank = [j.replace(
    '-', '') if re.match(r'^[4-6]([0-9]){3}-[0-9]{4}-[0-9]{4}-[0-9]{4}$', j) else j for j in tab]
print ('\n').join(['Valid' if(re.search(reg, uuid) and not re.search(
    reg_not, uuid)) else 'Invalid' for uuid in tab_bank])
