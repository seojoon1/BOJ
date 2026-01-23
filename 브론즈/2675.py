n = int(input())
for _ in range(n):
  a , b = input().split()
  for _ in range(len(b)):
    for i in range(len(a)):
      print(b[_] * int(a), end='')
  print()