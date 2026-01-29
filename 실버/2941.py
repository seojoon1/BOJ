s = input()
x = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
n = 0
for i in x:
  s = s.replace(i, " ") #특정 문자(i)를 공백(" ")으로 바꿈
n = len(s) #공백을 하나의 문자로 판단 후 길이 계산
print(n)