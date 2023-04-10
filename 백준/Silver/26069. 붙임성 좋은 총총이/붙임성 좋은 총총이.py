n = int(input())
dic = {'ChongChong': 1}
sum = 0

for i in range(n) :
  arr = input().split()
  # dic에 있는지 확인
  for j in arr :
    if j not in dic :
      dic[j] = 0
  if (dic[arr[0]] == 1) | (dic[arr[1]] == 1) :
    dic[arr[0]] = 1
    dic[arr[1]] = 1

for key in dic :
  sum += dic[key]

print(sum)