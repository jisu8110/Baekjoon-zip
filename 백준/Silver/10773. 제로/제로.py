count = int(input()) 
arr = [] 

for i in range(count) : 
    num = int(input())
    if(num == 0): #num이 0이면 pop
        arr.pop()
    else :
        arr.append(num) #그게 아니라면 append = push
        
print(sum(arr))