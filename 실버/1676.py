import math
n = int(input())
x = 0
f = math.factorial(n)
for i in range(len(str(f))):
  if str(f)[-i-1] == "0":
    x += 1
  else:
    break
print(x)