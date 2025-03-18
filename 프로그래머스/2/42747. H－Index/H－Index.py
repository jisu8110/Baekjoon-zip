def solution(citations):
    citations.sort(reverse=True)  # 내림차순 정렬
    for i, citation in enumerate(citations):
        if i >= citation:
            return i
    return len(citations)