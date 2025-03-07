from typing import List, Tuple

def solution(ecoli_data: List[Tuple[int, int, int, str, int]]) -> int:
    """
    2번 형질이 없으면서 1번이나 3번 형질을 가진 대장균 개체 수를 반환하는 함수
    
    Args:
        ecoli_data (List[Tuple[int, int, int, str, int]]): 대장균 데이터 리스트
            각 튜플은 (ID, PARENT_ID, SIZE_OF_COLONY, DIFFERENTIATION_DATE, GENOTYPE) 형식
            
    Returns:
        int: 조건을 만족하는 대장균 개체 수
        
    Examples:
        >>> solution([(1, None, 10, "2019/01/01", 8),
        ...          (2, None, 2, "2019/01/01", 15),
        ...          (3, 2, 100, "2020/01/01", 1),
        ...          (4, 2, 16, "2020/01/01", 13)])
        2
    """
    answer = 0
    return answer

def test_solution():
    """
    solution 함수를 테스트하는 함수
    """
    # 테스트 케이스 1: 기본 케이스
    ecoli_data1 = [
        (1, None, 10, "2019/01/01", 8),   # 1000₍₂₎ - 4번 형질만
        (2, None, 2, "2019/01/01", 15),   # 1111₍₂₎ - 1,2,3,4번 형질
        (3, 2, 100, "2020/01/01", 1),     # 0001₍₂₎ - 1번 형질만
        (4, 2, 16, "2020/01/01", 13)      # 1101₍₂₎ - 1,3,4번 형질
    ]
    assert solution(ecoli_data1) == 2, "ID 3, 4가 조건을 만족합니다."
    
    # 테스트 케이스 2: 조건을 만족하는 대장균이 없는 경우
    ecoli_data2 = [
        (1, None, 10, "2019/01/01", 8),   # 1000₍₂₎ - 4번 형질만
        (2, None, 2, "2019/01/01", 2),    # 0010₍₂₎ - 2번 형질만
        (3, 2, 100, "2020/01/01", 10)     # 1010₍₂₎ - 2,4번 형질
    ]
    assert solution(ecoli_data2) == 0, "조건을 만족하는 대장균이 없습니다."
    
    print("모든 테스트 케이스 통과!")

if __name__ == "__main__":
    test_solution() 