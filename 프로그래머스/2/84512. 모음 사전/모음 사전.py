def solution(word):
    answer = 0
    
    dictionary = []
    alphabet = ['A','E','I','O','U']
    
    def dfs(cnt, word):
        if cnt == 5:
            return
        for i in range(len(alphabet)):
            dictionary.append(word+alphabet[i])
            dfs(cnt+1, word+alphabet[i])
        
    
    dfs(0, '')
    
    return dictionary.index(word)+1