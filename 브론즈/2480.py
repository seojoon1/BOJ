import sys
ju = list(map(int, sys.stdin.readline().split()))

if ju[0] == ju[1] == ju[2]:
    print(10000 + ju[0] * 1000)
elif ju[0] == ju[1] or ju[0] == ju[2] or ju[1] == ju[2]:
    if ju[0] == ju[1] or ju[0] == ju[2]:
        print(1000 + ju[0] * 100)
    elif ju[1] == ju[2]:
        print(1000 + ju[1] * 100)
else:
    print(max(ju) * 100)