import sys
n = int(sys.stdin.readline())
ar = []
for i in range(n):
    h, name = sys.stdin.readline().rstrip().split()
    ar.append([int(h),name])
ar.sort(key = lambda x: (x[0])) #데이터를 정렬할 때 0번째 요소를 사용한다
for h, name in ar:
    print(h, name)