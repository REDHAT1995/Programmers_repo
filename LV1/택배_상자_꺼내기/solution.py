def get_position(num: int, w: int):
    """
    상자 번호를 입력받아 해당 상자의 층과 행을 반환합니다.
    
    Args:
        num (int): 상자 번호
        w (int): 각 층의 상자 개수
        
    Returns:
        tuple[int, int]: (층, 행) 튜플
    """
    num_floor = (num - 1) // w  # 선택한 상자의 층 수를 계산 (가장 아래 층은 0)
    
    # 선택한 상자의 행 수를 계산
    # 층이 짝수인지 홀수인지에 따라 행 수의 방향이 다름
    if num_floor % 2 == 0:  # 짝수일 경우
        num_row = (num - 1) % w
    else:
        num_row = (w - 1) - ((num - 1) % w)  # 홀수일 경우
        
    return (num_floor, num_row)

def solution(n: int, w: int, num: int) -> int:
    """
    택배 상자를 꺼내기 위해 필요한 상자의 총 개수를 계산합니다.
    
    Args:
        n (int): 창고에 있는 택배 상자의 개수 (2 ≤ n ≤ 100)
        w (int): 가로로 놓는 상자의 개수 (1 ≤ w ≤ 10)
        num (int): 꺼내려는 택배 상자의 번호 (1 ≤ num ≤ n)
        
    Returns:
        int: 꺼내야 하는 상자의 총 개수
        
    Raises:
        ValueError: 입력값이 제약 조건을 만족하지 않는 경우
    """
    # 입력값 검증
    if not (2 <= n <= 100 and 1 <= w <= 10 and 1 <= num <= n):
        raise ValueError("Invalid input parameters")
    
    answer = 0
    num_floor, num_row = get_position(num, w) # 목표 상자의 층과 행

    for i in range(1, n+1):
        cur_floor, cur_row = get_position(i, w) # 현재 상자의 층과 행
        # 현재 상자 층이 목표 상자 층보다 크거나 같고, 행이 같으면 꺼내야 하는 상자의 개수를 증가
        if cur_floor >= num_floor: 
            if cur_row == num_row:     
                answer += 1
                
    return answer

def test_solution():
    """테스트 케이스를 실행합니다."""
    # 테스트 케이스 1
    assert solution(22, 6, 8) == 3, "테스트 케이스 1 실패"
    
    # 테스트 케이스 2
    assert solution(13, 3, 6) == 4, "테스트 케이스 2 실패"
    
    # 경계값 테스트
    assert solution(2, 1, 1) == 2, "경계값 테스트 1 실패"
    assert solution(100, 10, 100) == 1, "경계값 테스트 2 실패"
    
    print("모든 테스트 케이스 통과!")

if __name__ == "__main__":
    test_solution() 