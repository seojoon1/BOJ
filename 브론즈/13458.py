import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a = a[:n]
d = 0
b,c = map(int, sys.stdin.readline().split())
for i in range(n):
    a[i] -= b
    d+=1
    if a[i] >0:
        if a[i] % c ==0:
            d += a[i]//c
        else:
            d += a[i]//c +1
print(d)
