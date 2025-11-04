S = input()
aList = [chr(i) for i in range(ord('a'),ord('z')+1)]
A = []
for i in aList:
    B = S.find(i)
    A.append(B)
print(*A, sep=' ')