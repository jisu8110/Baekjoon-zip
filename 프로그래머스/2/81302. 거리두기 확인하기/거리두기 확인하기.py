def solution(places):
    def check_distance(place, row, col):
        # 상하좌우 방향
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # 거리 1인 경우 체크
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < 5 and 0 <= nc < 5:
                if place[nr][nc] == 'P':
                    return False
                
        # 거리 2인 경우 체크
        # 상하좌우 거리 2
        for dr, dc in directions:
            nr, nc = row + (dr * 2), col + (dc * 2)
            if 0 <= nr < 5 and 0 <= nc < 5:
                if place[nr][nc] == 'P':
                    # 중간에 파티션이 있는지 확인
                    if place[row + dr][col + dc] != 'X':
                        return False
                        
        # 대각선 방향 체크
        diagonal = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dr, dc in diagonal:
            nr, nc = row + dr, col + dc
            if 0 <= nr < 5 and 0 <= nc < 5:
                if place[nr][nc] == 'P':
                    # 두 방향 모두 파티션이어야 함
                    if place[row + dr][col] != 'X' or place[row][col + dc] != 'X':
                        return False
                        
        return True

    answer = []
    for place in places:
        is_safe = True
        for row in range(5):
            for col in range(5):
                if place[row][col] == 'P':
                    if not check_distance(place, row, col):
                        is_safe = False
                        break
            if not is_safe:
                break
        answer.append(1 if is_safe else 0)
    
    return answer