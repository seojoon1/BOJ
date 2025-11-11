import sys
a = []
b = [1, 2, 3, 4, 5]
n = int(sys.stdin.readline())
for i in range(n):
    y = int(sys.stdin.readline())
    a.append(y)
a_set = set(a)
a = list(a_set)
a_sort = sorted(a)
if a != b:
    print("YES")
else:
    print("NO")
