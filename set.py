n = input()
s = set(map(int, raw_input().split()))
length = input()
for i in range(length):
    cmd=map(str,raw_input().split())
    if cmd[0] == 'pop':
        eval("s."+cmd[0]+"()")
    else:
        eval("s."+cmd[0]+"("+cmd[1]+")")
print sum(s)
