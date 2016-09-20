n = input()
s = set(map(int, raw_input().split()))
m = input()
s1 = set(map(int, raw_input().split()))
print len(s.difference(s1))

# remplacer difference par union ou intersection ou symmetric_difference
