import sys
input = sys.stdin.readline

N, M = input().split() # 입력받은 값을 공백을 기준으로 분리
N = int(N)
M = int(M)

dic = {} # 입력된 단어

for _ in range(N) :
    word = input().rstrip()
    if len(word) >= M :
        if word in dic :
            dic[word] += 1
        else :
            dic[word] = 1
    else :
      continue

dic = sorted(dic.items(), key=lambda x: (-x[1], -len(x[0]), x[0])) # reverse = 내림차순

for i in dic :
  print(i[0])