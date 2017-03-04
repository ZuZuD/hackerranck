#!/usr/bin/env python
import re

string = raw_input()
i,error=0,0
while i < len(string)-2:
  if string[i] != "S":
    error+=1
  if string[i+1] != "O":
    error+=1
  if string[i+2] != "S":
    error+=1
  i+=3
print error
