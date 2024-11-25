def solution(numbers):
    
    alphabet = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    target = ''
    answer = ''
    
    for i in numbers:
        target += i
        if target in alphabet:
            answer += str(alphabet.index(target))
            target = ''
    
    return int(answer)