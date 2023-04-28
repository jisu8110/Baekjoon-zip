N, K = map(int, input().split()) 
coin = list()
count = 0

for i in range(N) :
    coin.append(int(input()))

for i in reversed(range(N)):
    count += K // coin[i]
    K = K % coin[i] 

print(count)