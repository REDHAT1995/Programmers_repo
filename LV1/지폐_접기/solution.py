from typing import List, Optional, Union

def fold_bill(bill: List[int]) -> List[int]:
    # 지폐 크기 정렬
    bill.sort()
    # 지폐 크기 절반으로 줄이기 
    bill[1] = bill[1] // 2
    # 지폐 크기 정렬
    bill.sort()
    return bill

def solution(wallet: List[int], bill: List[int]) -> int:
    """
    지폐를 지갑에 넣기 위해 필요한 최소 접기 횟수를 계산하는 함수
    
    Args:
        wallet (List[int]): 지갑의 가로, 세로 크기를 담은 정수 리스트
        bill (List[int]): 지폐의 가로, 세로 크기를 담은 정수 리스트
        
    Returns:
        int: 지폐를 지갑에 넣기 위해 필요한 최소 접기 횟수
        
    Raises:
        ValueError: wallet이나 bill의 길이가 2가 아닌 경우
                   wallet이나 bill의 값이 제한사항을 벗어나는 경우
        
    Examples:
        >>> solution([30, 15], [26, 17])
        1
        >>> solution([50, 50], [100, 241])
        4
    """
    # 입력값 검증
    if len(wallet) != 2 or len(bill) != 2:
        raise ValueError("wallet과 bill의 길이는 2여야 합니다.")
    
    if not all(10 <= x <= 100 for x in wallet):
        raise ValueError("wallet의 값은 10 이상 100 이하여야 합니다.")
    
    if not all(10 <= x <= 2000 for x in bill):
        raise ValueError("bill의 값은 10 이상 2000 이하여야 합니다.")
    
    bill.sort() # 지폐 크기 정렬
    wallet.sort() # 지갑 크기 정렬
    
    answer = 0
    
    while bill[0] > wallet[0] or bill[1] > wallet[1]: # 지폐가 지갑에 들어갈 때까지 반복
        bill = fold_bill(bill) # 지폐 접기
        print(f"answer: {answer}, bill: {bill}, wallet: {wallet}")        
        answer += 1
        
    print(f"answer: {answer}")
    return answer

def test_solution():
    """
    solution 함수의 테스트를 수행하는 함수
    
    테스트 케이스:
    1. 기본 테스트 케이스
    2. 경계값 테스트 케이스
    3. 예외 케이스
    """
    # 테스트 케이스 1: 기본 케이스
    assert solution([30, 15], [26, 17]) == 1
    assert solution([50, 50], [100, 241]) == 4
    
    # 테스트 케이스 2: 경계값 케이스
    assert solution([10, 10], [10, 10]) == 0
    assert solution([100, 100], [2000, 2000]) == 10
    
    # 테스트 케이스 3: 예외 케이스
    try:
        solution([30], [26, 17])
        assert False, "길이가 2가 아닌 경우 예외가 발생해야 합니다."
    except ValueError:
        pass
    
    try:
        solution([30, 15], [9, 17])
        assert False, "bill의 값이 10 미만인 경우 예외가 발생해야 합니다."
    except ValueError:
        pass
    
    print("모든 테스트 케이스 통과!")

if __name__ == "__main__":
    test_solution() 