import sys
dataa = []
n = int(sys.stdin.readline())
for i in range(n):
    data = int(sys.stdin.readline())
    dataa.append(data)

dataa.sort()
for i in dataa:
    print(i)