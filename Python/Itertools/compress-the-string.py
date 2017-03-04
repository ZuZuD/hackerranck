#!/usr/bin/env python
print ' '.join([str((len(list(y)), int(x))) for x, y in groupby(raw_input())])
