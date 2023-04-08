import re   #re 모듈 import
n = int(input())  #input함수는 기본적으로 입력받은 값을 str으로 취급
result = 0

for i in range(n) :
  word = input()
  while len(word) != 0 :
    first = word[0]
    word = re.sub('^'+ first +'+', "", word)
    if first in word :
      break
    elif len(word) == 0 :
      result = result + 1

print(result)