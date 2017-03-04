#!/usr/bin/env python3

time = input().strip().split(':')
meridium = time[-1][-2:]
time = [int(i.replace(meridium,'')) for i in time]
if meridium == 'PM':
    if time[0] != 12:
      time[0] = time[0]+12  
    print('%02d:%02d:%02d' %tuple(i for i in time))
else:
    if time[0] == 12:
        time[0] = 0
    print('%02d:%02d:%02d' %tuple(i for i in time))
