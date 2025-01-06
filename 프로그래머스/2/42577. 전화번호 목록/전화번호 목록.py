# def solution(phone_book):
    
#     phone_book.sort(key = lambda x: int(x))
    
#     for i in range(len(phone_book)-1):
#         for j in range(i+1, len(phone_book)):
#             if phone_book[i] in phone_book[j] and phone_book[j].index(phone_book[i]) == 0:
#                 return False
            
#     return True

def solution(phone_book):
    phone_book.sort()  # 문자열 기준으로 정렬
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True