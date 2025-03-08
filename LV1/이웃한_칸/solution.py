def solution(board: list, h: int, w: int) -> int:
    """
    주어진 보드에서 특정 위치(h, w)의 이웃한 칸들 중 같은 색상의 개수를 반환하는 함수
    
    Args:
        board (list): 각 칸의 색상이 담긴 2차원 문자열 리스트
        h (int): 선택한 칸의 세로 위치
        w (int): 선택한 칸의 가로 위치
        
    Returns:
        int: 이웃한 칸들 중 같은 색상의 개수
        
    Examples:
        >>> solution([["blue", "red", "orange", "red"], 
                     ["red", "red", "blue", "orange"], 
                     ["blue", "orange", "red", "red"], 
                     ["orange", "orange", "red", "blue"]], 1, 1)
        2
    """
    # 같은 색상의 이웃한 칸 개수를 저장할 변수
    answer = 0
    
    # 현재 위치(h,w)의 색상 저장
    current_color = board[h][w]
    
    # 상하좌우 이동을 위한 방향 배열
    # dh: 세로 방향 이동 [-1: 위, 1: 아래, 0: 제자리]
    # dw: 가로 방향 이동 [-1: 왼쪽, 1: 오른쪽, 0: 제자리]
    dh = [0, 1, -1, 0]  # 오른쪽, 아래, 위, 왼쪽 순서
    dw = [1, 0, 0, -1]
    
    # 4방향(상하좌우)의 이웃한 칸 확인
    for i in range(4):
        # 확인할 이웃한 칸의 좌표 계산
        h_check = h + dh[i]  # 세로 좌표
        w_check = w + dw[i]  # 가로 좌표
        
        # 계산된 좌표가 보드 범위 내에 있는지 확인
        if 0 <= h_check < len(board) and 0 <= w_check < len(board[0]):
            # 이웃한 칸의 색상이 현재 칸의 색상과 같은지 확인
            if board[h_check][w_check] == current_color:
                answer += 1  # 같은 색상이면 카운트 증가
    
    # 찾은 같은 색상의 이웃한 칸 개수 반환
    return answer


# 테스트 케이스
def test_solution():
    """
    solution 함수를 테스트하는 함수
    """
    # 테스트 케이스 1
    assert solution(
        [["blue", "red", "orange", "red"],
         ["red", "red", "blue", "orange"],
         ["blue", "orange", "red", "red"],
         ["orange", "orange", "red", "blue"]], 
        1, 1
    ) == 2
    
    # 테스트 케이스 2
    assert solution(
        [["yellow", "green", "blue"],
         ["blue", "green", "yellow"],
         ["yellow", "blue", "blue"]], 
        0, 1
    ) == 1
    
    print("모든 테스트 케이스 통과!")

if __name__ == "__main__":
    test_solution() 