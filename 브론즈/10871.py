
n, x = map(int, input().split())
a = list(map(int, input().split()))
a = a[:n]
b=[]
for i in a:
    if i < x:
        b.append(i)
print(' '.join(map(str, b)))