word = input().upper()
word_unique = list(set(word))
cnt = []

for i in word_unique :
  n = word.count(i)
  cnt.append(n)

if cnt.count(max(cnt)) != 1 :
  print("?")
else :
  print(word_unique[cnt.index(max(cnt))])