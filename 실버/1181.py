import sys
n = int(sys.stdin.readline())
ar = []
for i in range(n):
    word = sys.stdin.readline().rstrip()
    ar.append(word)
set_ar = set(ar)
list_ar = list(set_ar)
sorted_ar = sorted(list_ar, key= lambda x : (len(x), x))
for word in sorted_ar:
    print(word)