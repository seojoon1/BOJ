import sys
input = sys.stdin.readline
n1 = int(input())
numSet1 = set(map(int, input().split()))
n2 = int(input())
numSet2 = list(map(int, input().split()))
for q in numSet2:
    if q in numSet1:
        print(1)
    else:
        print(0) 