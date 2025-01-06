def solution(babbling):
    
    pronaunce = ['aya', 'ye', 'woo', 'ma']
    count = 0
    
    for babb in babbling:
        print(babb)
        for i in pronaunce:
            babb = babb.replace(i, " ")
            print(babb)
        if babb.strip() == "":
            count += 1
    
    return count