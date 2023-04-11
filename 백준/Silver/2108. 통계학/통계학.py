import sys
n = int(sys.stdin.readline())
arr = [] # 입력한 값
dic = {} # 중복되는 값
sum = 0
many_result = 0 # 최빈값

for i in range(n) :
  k = int(sys.stdin.readline())
  if k in dic :
    dic[k] += 1
  elif k in arr :
    dic[k] = 1
  arr.append(k)
  sum += k
arr.sort()

many = [key for key, value in dic.items() if max(dic.values()) == value]
many.sort()

if len(dic) == 0 :
  if len(arr) == 1 :
    many_result = arr[0]
  else :
    many_result = arr[1]
elif len(many) == 1 :
  many_result = many[0]
else :
  many_result = many[1]

# 결과 출력
print(round(sum/n)) # 산술평균
print(arr[int((n-1)/2)]) # 중앙값
print(many_result) # 최빈값
print(arr[n-1] - arr[0]) # 범위