#!/usr/bin/env python

import re

pattern = [r'([A-Za-z0-9]){10}', r'([A-Z].*){2}', r'([0-9].*){3}']
reg = map(re.compile, pattern)
length = input()
tab_uuid = [raw_input() for j in range(length)]
print ('\n').join(['Valid' if all([re.search(r, uuid) for r in reg]) and not re.search(
    r'.*(.).*\1', uuid) else 'Invalid' for uuid in tab_uuid])
