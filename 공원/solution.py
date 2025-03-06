from typing import List

def solution(mats: List[int], park: List[List[str]]) -> int:
    """
    공원에 놓을 수 있는 가장 큰 돗자리의 크기를 찾는 함수
    
    Args:
        mats (List[int]): 가지고 있는 돗자리들의 한 변의 길이
        park (List[List[str]]): 공원의 자리 배치도
        
    Returns:
        int: 놓을 수 있는 가장 큰 돗자리의 한 변 길이, 불가능한 경우 -1
    """
    answer = 0
    return answer

def test_solution():
    """
    solution 함수의 테스트를 수행하는 함수
    """
    # 테스트 케이스 1: 기본 케이스
    mats1 = [5, 3, 2]
    park1 = [
        ["A", "A", "-1", "B", "B", "B", "B", "-1"],
        ["A", "A", "-1", "B", "B", "B", "B", "-1"],
        ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"],
        ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"],
        ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"],
        ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"]
    ]
    assert solution(mats1, park1) == 3
    
    # 테스트 케이스 2: 돗자리를 놓을 수 없는 경우
    mats2 = [5, 3, 2]
    park2 = [
        ["A", "A", "B", "B", "B", "B", "B", "B"],
        ["A", "A", "B", "B", "B", "B", "B", "B"],
        ["B", "B", "B", "B", "B", "B", "B", "B"],
        ["D", "D", "B", "B", "B", "B", "E", "B"],
        ["D", "D", "B", "B", "B", "B", "B", "F"],
        ["D", "D", "B", "B", "B", "B", "E", "B"]
    ]
    assert solution(mats2, park2) == -1
    
    print("모든 테스트 케이스 통과!")

if __name__ == "__main__":
    test_solution() 