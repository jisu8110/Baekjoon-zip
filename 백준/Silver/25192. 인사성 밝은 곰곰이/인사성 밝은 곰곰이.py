n = int(input())
dic = {} 
count = 0 # 이모티콘 횟수

for i in range(n) :
  chat = input()
  if chat == 'ENTER' : # 새로 입장
    dic = {}
  else :
    if chat not in dic :
      dic[chat] = 1
      count += 1

print(count)