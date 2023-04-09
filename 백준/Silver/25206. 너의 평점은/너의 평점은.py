arr = []
for i in range(20) :
  arr.append(input().split())
total = 0 # 학점 총합
sum = 0 # 학점x과목평점

# 과목수만큼 반복
for i in range(len(arr)) :
  # 과목평점을 숫자로
  score_str = arr[i-1][2]
  if score_str == 'A+' : score = 4.5
  elif score_str == 'A0' : score = 4.0
  elif score_str == 'B+' : score = 3.5
  elif score_str == 'B0' : score = 3.0
  elif score_str == 'C+' : score = 2.5
  elif score_str == 'C0' : score = 2.0
  elif score_str == 'D+' : score = 1.5
  elif score_str == 'D0' : score = 1.0 
  else : score = 0.0
  # 학점x과목평점
  sum += float(arr[i-1][1]) * score
  # 학점 총합  # P인 과목은 계산에서 제외
  if score_str != 'P' :
    total += float(arr[i-1][1])

# 결과 계산
print(sum/total)