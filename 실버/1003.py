import sys
input = sys.stdin.readline

N = int(input())
for i in range(N):
  arr = [1,1]
  T = int(input())
  if T == 1:
    arr = [0,1]
    print(arr[0], arr[1])
    continue
  elif T == 0:
    arr = [1,0]
    print(arr[0], arr[1])
    continue
  else:
    for j in range(T-2):
      x = arr[1] #
      arr[1] = arr[0] + arr[1]
      arr[0] = x
    print(arr[0], arr[1])
    continue