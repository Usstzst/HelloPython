

import sys

IP  = [int(t) for t in sys.stdin.readline().split('.')]
n = []
for i in range(len(IP)):
    if IP[i]>0 and IP[i]<256:
        n.append(IP[i])


if len(IP)==len(n):
    print 'YES'
else:
    print 'NO'
