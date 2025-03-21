def solution(n, computers):
    network = 0
    
    def dfs(k):
        
        if computers[k].count(1) == 1:
            return
        for i in range(n):
            if computers[k][i] == 1:
                computers[k][i] = -1
                dfs(i)
                
    for i in range(n):
        if 1 in computers[i]:
            dfs(i)
            network += 1
    
    return network