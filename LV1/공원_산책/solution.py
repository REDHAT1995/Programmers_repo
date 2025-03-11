from typing import List

def solution(park: List[str], routes: List[str]) -> List[int]:
    """
    공원 산책 문제를 해결하는 함수
    
    Args:
        park (List[str]): 공원의 지도를 나타내는 문자열 배열
        routes (List[str]): 수행할 명령어가 담긴 문자열 배열
        
    Returns:
        List[int]: 최종적으로 도착할 위치의 좌표 [세로 방향 좌표, 가로 방향 좌표]
        
    Raises:
        ValueError: 입력값이 제한사항을 벗어나는 경우
        
    Examples:
        >>> solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"])
        [2, 1]
    """
    # 입력값 검증
    if not (3 <= len(park) <= 50) or not all(3 <= len(row) <= 50 for row in park):
        raise ValueError("공원의 크기가 제한사항을 벗어났습니다.")
    
    if not (1 <= len(routes) <= 50):
        raise ValueError("명령어의 개수가 제한사항을 벗어났습니다.")
    
    answer = [0, 0]
    return answer

def test_solution():
    """
    solution 함수의 테스트를 수행하는 함수
    
    테스트 케이스:
    1. 기본 테스트 케이스
    2. 장애물이 있는 경우
    3. 공원을 벗어나는 경우
    """
    # 테스트 케이스 1: 기본 이동
    park1 = ["SOO","OOO","OOO"]
    routes1 = ["E 2","S 2","W 1"]
    assert solution(park1, routes1) == [2,1], "기본 이동 테스트 실패"
    
    # 테스트 케이스 2: 장애물이 있는 경우
    park2 = ["SOO","OXX","OOO"]
    routes2 = ["E 2","S 2","W 1"]
    assert solution(park2, routes2) == [0,1], "장애물 처리 테스트 실패"
    
    # 테스트 케이스 3: 공원을 벗어나는 경우
    park3 = ["OSO","OOO","OXO","OOO"]
    routes3 = ["E 2","S 3","W 1"]
    assert solution(park3, routes3) == [0,0], "경계 처리 테스트 실패"
    
    # 예외 테스트: 잘못된 입력
    try:
        solution(["S"], ["E 1"])
        assert False, "잘못된 공원 크기 검증 실패"
    except ValueError:
        pass
    
    print("모든 테스트 케이스 통과!")

if __name__ == "__main__":
    test_solution() 